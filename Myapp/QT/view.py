from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt, Signal
from random import randint

class View(QMainWindow):
    button_clicked = Signal()

    def __init__(self):
        super(View, self).__init__()
        self.setWindowTitle("MVC Example")
        self.resize(400, 300)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Change Color")
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.button_clicked.emit)

    def update_label(self, text):
        self.label.setText(text)

    def change_widget_color(self):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        color = f"background-color: rgb({red}, {green}, {blue})"
        self.widget.setStyleSheet(color)