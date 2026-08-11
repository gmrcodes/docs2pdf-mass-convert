# 📄 Word2PDF Mass Convert

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Version](https://img.shields.io/badge/version-0.2.0-green.svg)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Platform Support](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

Aplicación de escritorio moderna y multiplataforma diseñada para convertir lotes de documentos Word (`.doc` y `.docx`) a formato PDF de manera rápida, sencilla y segura. Construida bajo el patrón de arquitectura **MVC (Modelo-Vista-Controlador)** con procesamiento asíncrono para garantizar la fluidez de la interfaz.

---

## 📸 Capturas de Pantalla

|                           Modo Claro                           |                           Modo Oscuro                            |
| :------------------------------------------------------------: | :--------------------------------------------------------------: |
| <img src="media/modo claro.png" width="400" alt="Modo claro"/> | <img src="media/modo oscuro.png" width="400" alt="Modo oscuro"/> |

|                                log                                 |                                Finalizada                                |
| :----------------------------------------------------------------: | :----------------------------------------------------------------------: |
| <img src="media/log convertion.png" width="400" alt="Modo claro"/> | <img src="media/convertion finished.png" width="400" alt="Modo oscuro"/> |

---

## ✨ Características Principales

- **Conversión por Lotes:** Procesa directorios completos con múltiples archivos `.doc` y `.docx` en cuestión de clics.
- **Interfaz Gráfica Moderna:** Desarrollada con CustomTkinter, compatible con el tema del sistema (modo claro y oscuro nativo).
- **Procesamiento Asíncrono (Multi-threading):** La interfaz permanece fluida y respondiendo en todo momento durante la conversión de archivos.
- **Logs y Progreso en Tiempo Real:** Visualización del progreso individual y consola de registro integrada.
- **Arquitectura Escalable (MVC):** Desacoplamiento total entre la lógica de negocio, la interfaz gráfica y los controladores de eventos.

---

## 🛠️ Tecnologías

- **Lenguaje:** [Python 3.10+](https://www.python.org/)
- **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **Motor de Conversión (Windows/macOS):** `docx2pdf` (vía Microsoft Word Interop)
- **Motor de Conversión (Linux/Multiplataforma):** LibreOffice CLI.
- **Empaquetado:** [PyInstaller](https://pyinstaller.org/)

---

## 📋 Requisitos del Sistema

### Requisito General

- **Python:** 3.10 o superior.

### Dependencias por Sistema Operativo

| Sistema Operativo         | Motor de Conversión Requerido | Comando de Instalación del Motor  |
| :------------------------ | :---------------------------- | :-------------------------------- |
| **Windows**               | Microsoft Word                | Instalador nativo de MS Office    |
| **Linux** (Debian/Ubuntu) | LibreOffice (`soffice`)       | `sudo apt install libreoffice -y` |
| **Linux** (Fedora/RHEL)   | LibreOffice (`soffice`)       | `sudo dnf install libreoffice -y` |
| **macOS**                 | Microsoft Word                | Instalador oficial de MS Office   |

---

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura **MVC** organizada en carpetas independientes:

```text
DOCS2PDF-MASS-CONVERT/
├── controller/
│   ├── __init__.py
│   └── converter_controller.py # Escucha eventos de la vista y coordina el modelo
├── model/
│   ├── __init__.py
│   └── converter_model.py      # Lógica de negocio, hilos y llamadas a motores de conversión
├── view/
│   ├── __init__.py
│   └── main_view.py            # Componentes gráficos y maquetación (CustomTkinter)
├── media/                      # Screenshots de la UI
├── .gitignore                  # Archivos ignorados por Git
├── LICENSE                     # Licencia del proyecto (GPLv3)
├── main.py                     # Punto de entrada principal
├── README.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias del proyecto
```

## 🚀 Instalación y Ejecución Local

### 1. Clonar el repositorio:

```bash

git clone https://github.com/gmrcodes/docs2pdf-mass-convert.git
cd word2pdf-masivo

```

### 2. Crear y activar el entorno virtual (opcional):

#### Linux / macOS:

```bash

python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias:

```bash

pip install -r requirements.txt
```

### Ejecutar la aplicación:

```bash

python main.py
```

## 📜 Licencia

Este proyecto está distribuido bajo la licencia GNU General Public License v3.0 (GPLv3). Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
