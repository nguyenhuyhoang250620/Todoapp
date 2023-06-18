from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import QPushButton,QWidget,QVBoxLayout
from PySide6.QtCore import Qt


class Button(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hoang")
        button = QPushButton("press")
        button1 = QPushButton("HELLO")

        button.clicked.connect(self.click)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.addWidget(button)
        main_layout.addWidget(button1)
        self.setLayout(main_layout)

        # Đặt nền cho widget
        self.setStyleSheet("background-color: #C0C0C0;")

    def click(self):
        print("hello")

