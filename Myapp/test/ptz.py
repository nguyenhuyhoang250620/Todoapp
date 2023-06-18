import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QFrame
from PySide6.QtCore import Qt

class DropDownWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập thuộc tính ban đầu cho widget
        self.is_hidden = False

        # Tạo frame chứa nút button
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)

        # Tạo layout dọc cho frame
        layout = QVBoxLayout(self.frame)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        # Tạo các nút button
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")

        # Thêm các nút button vào layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        # Tạo nút dropdown
        self.dropdown_button = QPushButton("Dropdown")
        self.dropdown_button.clicked.connect(self.toggle_widget)

        # Tạo layout dọc chính cho widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.dropdown_button)
        main_layout.addWidget(self.frame)

    def toggle_widget(self):
        if self.is_hidden:
            self.frame.setVisible(True)
            self.is_hidden = False
        else:
            self.frame.setVisible(False)
            self.is_hidden = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget Dropdown")
        self.setGeometry(100, 100, 300, 200)

        # Tạo dropdown widget
        dropdown_widget = DropDownWidget()

        # Thiết lập widget chính của cửa sổ là dropdown widget
        self.setCentralWidget(dropdown_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())