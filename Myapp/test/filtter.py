import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QListWidget, QComboBox, QWidget
from PySide6.QtCore import Qt

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tìm kiếm PySide6")
        self.setGeometry(100, 100, 300, 200)

        # Tạo một widget chính và layout dọc cho nó
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # Tạo combobox lọc
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("Tất cả")
        self.filter_combo.addItem("Chữ")
        self.filter_combo.addItem("Số")
        self.filter_combo.currentIndexChanged.connect(self.filter_list)

        # Tạo danh sách tìm kiếm
        self.search_list = QListWidget()

        # Thêm dữ liệu vào danh sách tìm kiếm
        data = ["John", "Jane", "Alex", "Emily", "Mark", "Sara", "123", "456", "789"]
        self.search_list.addItems(data)
        self.search_list.setProperty("original_items", data)

        # Thêm combobox lọc và danh sách tìm kiếm vào layout dọc
        main_layout.addWidget(self.filter_combo)
        main_layout.addWidget(self.search_list)

        # Thiết lập widget chính của cửa sổ là main_widget
        self.setCentralWidget(main_widget)

    def filter_list(self):
        filter_text = self.filter_combo.currentText()

        search_list = self.search_list
        original_items = search_list.property("original_items")

        search_list.clear()

        if filter_text == "Tất cả":
            search_list.addItems(original_items)
        elif filter_text == "Chữ":
            filtered_items = [item for item in original_items if item.isalpha()]
            search_list.addItems(filtered_items)
        elif filter_text == "Số":
            filtered_items = [item for item in original_items if item.isdigit()]
            search_list.addItems(filtered_items)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())