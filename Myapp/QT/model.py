from PySide6.QtCore import QObject, Signal

class Model(QObject):
    text_changed = Signal(str)

    def __init__(self):
        super(Model, self).__init__()
        self._text = ""

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.text_changed.emit(value)