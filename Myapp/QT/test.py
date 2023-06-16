from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor,QStandardItemModel,QStandardItem
from PySide6.QtWidgets import QStyledItemDelegate, QApplication, QTableView



class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Ghi đè phương thức paint để vẽ dữ liệu vào ô của mục

        # Lấy dữ liệu từ mô hình
        data = index.data(Qt.DisplayRole)

        # Vẽ dữ liệu vào ô
        painter.save()
        painter.fillRect(option.rect, QColor(255, 255, 255))  # Màu nền cho ô
        painter.drawText(option.rect, Qt.AlignCenter, str(data))  # Hiển thị dữ liệu
        painter.restore()

    def sizeHint(self, option, index):
        # Ghi đè phương thức sizeHint để thiết lập kích thước cho ô

        # Thiết lập kích thước ô là 100x30
        return option.rect.width(), option.rect.height()


if __name__ == "__main__":
    app = QApplication([])

    # Tạo mô hình và dữ liệu
    data = [
        ["Alice", 25],
        ["Bob", 30],
        ["Charlie", 35],
    ]
    model = QStandardItemModel()
    for row in data:
        item1 = QStandardItem(row[0])
        item2 = QStandardItem(str(row[1]))
        model.appendRow([item1, item2])

    # Tạo bảng và thiết lập delegate
    table_view = QTableView()
    table_view.setModel(model)
    delegate = CustomDelegate()
    table_view.setItemDelegate(delegate)

    table_view.show()
    app.exec()