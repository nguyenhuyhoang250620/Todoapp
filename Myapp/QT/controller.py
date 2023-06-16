from model import Model
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.update_label(self.model.text)
        self.view.show()

        self.model.text_changed.connect(self.view.update_label)
        self.view.button_clicked.connect(self.view.change_widget_color)