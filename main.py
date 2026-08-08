from model.converter_model import ConverterModel
from view.main_view import MainView
from controller.converter_controller import ConverterController

APP_VERSION = '0.2.0'

def main():
    model = ConverterModel()
    view = MainView()
    # El controlador vincula el modelo y la vista
    ConverterController(model, view)

    view.mainloop()

if __name__ == "__main__":
    main()