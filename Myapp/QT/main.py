from PySide6.QtWidgets import QApplication
from model import Model
from view import View
from controller import Controller

if __name__ == "__main__":
    app = QApplication([])

    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.view.button_clicked.connect(controller.view.change_widget_color)

    app.exec()