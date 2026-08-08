import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Convertidor Masivo de Word a PDF")
        self.geometry("640x480")
        self.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        # Título principal
        self.lbl_title = ctk.CTkLabel(
            self, 
            text="Convertidor de Documentos Word a PDF", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.lbl_title.pack(pady=(20, 15))

        # --- Carpeta Origen ---
        self.frame_input = ctk.CTkFrame(self)
        self.frame_input.pack(padx=20, pady=10, fill="x")

        self.btn_select_input = ctk.CTkButton(
            self.frame_input, 
            text="Seleccionar Carpeta Origen", 
            width=180
        )
        self.btn_select_input.pack(side="left", padx=10, pady=10)

        self.lbl_input_path = ctk.CTkLabel(
            self.frame_input, 
            text="No se ha seleccionado ninguna carpeta", 
            anchor="w",
            text_color="gray"
        )
        self.lbl_input_path.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        # --- Carpeta Destino ---
        self.frame_output = ctk.CTkFrame(self)
        self.frame_output.pack(padx=20, pady=10, fill="x")

        self.btn_select_output = ctk.CTkButton(
            self.frame_output, 
            text="Seleccionar Carpeta Destino", 
            width=180
        )
        self.btn_select_output.pack(side="left", padx=10, pady=10)

        self.lbl_output_path = ctk.CTkLabel(
            self.frame_output, 
            text="Igual a la carpeta origen (por defecto)", 
            anchor="w",
            text_color="gray"
        )
        self.lbl_output_path.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        # --- Control de Conversión ---
        self.btn_convert = ctk.CTkButton(
            self, 
            text="Iniciar Conversión", 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#2FA572", 
            hover_color="#1E7A52",
            height=40
        )
        self.btn_convert.pack(padx=20, pady=15, fill="x")

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.pack(padx=20, pady=(0, 10), fill="x")
        self.progress_bar.set(0)

        # --- Caja de Logs ---
        self.txt_log = ctk.CTkTextbox(self, height=120, state="disabled")
        self.txt_log.pack(padx=20, pady=(0, 20), fill="both", expand=True)

    # --- API pública de la vista para el controlador ---
    def set_input_path_text(self, text: str, active: bool = True):
        color = "white" if active else "gray"
        self.lbl_input_path.configure(text=text, text_color=color)

    def set_output_path_text(self, text: str, active: bool = True):
        color = "white" if active else "gray"
        self.lbl_output_path.configure(text=text, text_color=color)

    def set_progress(self, value: float):
        self.progress_bar.set(value)

    def append_log(self, message: str):
        self.txt_log.configure(state="normal")
        self.txt_log.insert("end", message + "\n")
        self.txt_log.see("end")
        self.txt_log.configure(state="disabled")

    def set_convert_button_state(self, state: str):
        self.btn_convert.configure(state=state)

    def ask_directory(self, title: str) -> str:
        return filedialog.askdirectory(title=title)

    def show_warning(self, title: str, message: str):
        messagebox.showwarning(title, message)

    def show_info(self, title: str, message: str):
        messagebox.showinfo(title, message)

    def show_error(self, title: str, message: str):
        messagebox.showerror(title, message)