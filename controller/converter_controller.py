from model.converter_model import ConverterModel
from view.main_view import MainView


class ConverterController:
    def __init__(self, model: ConverterModel, view: MainView):
        self.model = model
        self.view = view

        # Conectar eventos de la UI con métodos del controlador
        self.view.btn_select_input.configure(command=self.on_select_input)
        self.view.btn_select_output.configure(command=self.on_select_output)
        self.view.btn_convert.configure(command=self.on_start_conversion)

    def on_select_input(self):
        folder = self.view.ask_directory("Seleccionar carpeta con archivos Word")
        if folder:
            self.model.input_folder = folder
            self.view.set_input_path_text(folder, active=True)
            if not self.model.output_folder:
                self.view.set_output_path_text(f"{folder} (por defecto)", active=False)

    def on_select_output(self):
        folder = self.view.ask_directory("Seleccionar carpeta de destino")
        if folder:
            self.model.output_folder = folder
            self.view.set_output_path_text(folder, active=True)

    def on_start_conversion(self):
        if not self.model.input_folder:
            self.view.show_warning("Advertencia", "Por favor, selecciona una carpeta de origen.")
            return

        self.view.set_convert_button_state("disabled")
        self.view.set_progress(0)

        origen = self.model.input_folder
        destino = self.model.output_folder if self.model.output_folder else self.model.input_folder

        # Delegar ejecución asíncrona al Modelo
        self.model.convert_folder_async(
            origen=origen,
            destino=destino,
            progress_cb=self._handle_progress,
            log_cb=self._handle_log,
            complete_cb=self._handle_complete,
            error_cb=self._handle_error
        )

    # --- Callbacks provenientes del Modelo ---
    def _handle_progress(self, value: float):
        self.view.set_progress(value)

    def _handle_log(self, message: str):
        self.view.append_log(message)

    def _handle_complete(self, total: int):
        self.view.set_convert_button_state("normal")
        if total > 0:
            self.view.show_info("Éxito", f"Se han convertido {total} archivo(s) a PDF.")

    def _handle_error(self, error_msg: str):
        self.view.set_convert_button_state("normal")
        self.view.show_error("Error", f"Ocurrió un error inesperado:\n{error_msg}")