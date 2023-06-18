import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QListWidget, QWidget
from PySide6.QtCore import Qt

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tìm kiếm PySide6")
        self.setGeometry(100, 100, 300, 200)

        # Tạo một widget chính và layout dọc cho nó
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # Tạo thanh tìm kiếm
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Nhập từ khóa tìm kiếm...")
        search_bar.textChanged.connect(self.filter_list)

        # Tạo danh sách tìm kiếm
        search_list = QListWidget()

        # Thêm dữ liệu vào danh sách tìm kiếm
        names = ["John", "Jane", "Alex", "Emily", "Mark", "Sara"]
        search_list.addItems(names)
        search_list.setProperty("original_items", names)

        # Thêm thanh tìm kiếm và danh sách tìm kiếm vào layout dọc
        main_layout.addWidget(search_bar)
        main_layout.addWidget(search_list)

        # Thiết lập widget chính của cửa sổ là main_widget
        self.setCentralWidget(main_widget)

    def filter_list(self, keyword):
        search_list = self.centralWidget().findChild(QListWidget)
        original_items = search_list.property("original_items")

        filtered_items = [item for item in original_items if keyword.lower() in item.lower()]
        
        search_list.clear()
        search_list.addItems(filtered_items)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())