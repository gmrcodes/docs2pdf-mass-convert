import os
import threading
from docx2pdf import convert


class ConverterModel:
    def __init__(self):
        self.input_folder = ""
        self.output_folder = ""

    def get_word_files(self, folder_path: str) -> list[str]:
        """Obtiene la lista de archivos Word válidos en la carpeta."""
        if not os.path.exists(folder_path):
            return []
        return [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.doc', '.docx')) and not f.startswith('~$')
        ]

    def convert_folder_async(self, origen: str, destino: str, progress_cb, log_cb, complete_cb, error_cb):
        """Ejecuta el proceso de conversión en un hilo secundario."""
        def _worker():
            try:
                archivos = self.get_word_files(origen)
                total_archivos = len(archivos)

                if total_archivos == 0:
                    log_cb("⚠️ No se encontraron archivos .doc o .docx en la carpeta seleccionada.")
                    complete_cb(0)
                    return

                log_cb(f"📋 Se encontraron {total_archivos} archivo(s) para procesar.")

                for i, archivo in enumerate(archivos, start=1):
                    ruta_doc = os.path.normpath(os.path.join(origen, archivo))
                    nombre_base = os.path.splitext(archivo)[0]
                    ruta_pdf = os.path.normpath(os.path.join(destino, f"{nombre_base}.pdf"))

                    log_cb(f"[{i}/{total_archivos}] Convirtiendo: {archivo}...")
                    convert(ruta_doc, ruta_pdf)

                    progreso = i / total_archivos
                    progress_cb(progreso)

                log_cb("✅ ¡Proceso finalizado con éxito!")
                complete_cb(total_archivos)

            except Exception as e:
                log_cb(f"❌ Error durante el proceso: {str(e)}")
                error_cb(str(e))

        thread = threading.Thread(target=_worker, daemon=True)
        thread.start()