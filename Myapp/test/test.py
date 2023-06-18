from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QStackedWidget, QVBoxLayout, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StackedWidget Example")

        # Tạo QTabWidget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Tạo QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Tạo QWidget con cho QStackedWidget
        self.widget = QWidget()
        self.label = QLabel("Overlay Widget")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.widget.setLayout(layout)

        # Thêm QWidget vào QStackedWidget
        self.stacked_widget.addWidget(self.widget)

        # Thêm QStackedWidget vào QTabWidget
        self.tab_widget.addTab(self.stacked_widget, "Tab 1")

        # Kích hoạt QStackedWidget
        self.tab_widget.setCurrentIndex(0)

        # Kết nối sự kiện thay đổi tab
        self.tab_widget.currentChanged.connect(self.handleTabChange)

    def handleTabChange(self, index):
        if index == 0:
            self.stacked_widget.setCurrentIndex(0)

# Tạo ứng dụng Qt
app = QApplication([])
# Tạo cửa sổ chính và hiển thị
window = MainWindow()
window.show()
# Chạy ứng dụng Qt
app.exec()