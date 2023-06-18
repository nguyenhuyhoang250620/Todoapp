from PySide6.QtCore import Qt,QSize
from PySide6.QtGui import QColor,QPixmap,QIcon,QTransform
from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton,QVBoxLayout, QTabWidget, QWidget, QTabBar, QLabel,QPushButton,QHBoxLayout

from button import Button


class SideMenu(QTabWidget):
    def __init__(self):
        super().__init__()

        
        self.setTabPosition(QTabWidget.West)  # Đặt vị trí tab ở phía tây (bên trái)

        # Tạo layout chính cho SideMenu


        # Tạo các tab và nội dung tương ứng
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        # Tạo QLabel để chứa ảnh
        image_label = QLabel(self)

        # Đường dẫn đến ảnh
        image_path = "Logo.png"

        # Tạo QPixmap từ đường dẫn ảnh
        pixmap = QPixmap(image_path)

        # Đặt kích thước tối đa cho QLabel
        max_width = 200  # Chiều rộng tối đa mong muốn
        max_height = 200  # Chiều cao tối đa mong muốn
        pixmap = pixmap.scaled(max_width, max_height)



        # Đặt các tab vào SideMenu
        self.addTab(self.tab1, "")
        self.addTab(self.tab2, "")
        self.addTab(self.tab3, "")
        self.addTab(self.tab4, "")
        
        self.setTabIcon(0, pixmap)
        self.setTabIcon(1, QIcon("Device_red.png"))
        self.setTabIcon(2, QIcon("Device_red.png"))
        self.setTabIcon(3, QIcon("Device_red.png"))
 

        # Thiết lập nội dung cho mỗi tab
        self.setTabContent(self.tab2, QLabel('lala'))
        # self.setTabContent(self.tab2, "This is Tab 2")
        # self.setTabContent(self.tab3, "This is Tab 3")

        # Đặt màu nền cho tab và nội dung
        self.setStyleSheet("QTabBar::tab { background-color: #C0C0C0; color: #333333; }"
                           "QTabWidget::pane { background-color: #ffffff; }")

        # Đặt chiều rộng của tab
        self.tabBar().setFixedWidth(150)

      


        self.tab_names = {
            1: "Device_red.png",
            2: "Device_red.png",
            3: "Device_red.png"
        }
        self.currentChanged.connect(self.onTabChanged)

        self.setTabIcon(1, QIcon("Device_white.png"))

        self.setTabToolTip(1, "Tab 1")
        self.setTabToolTip(2, "Tab 2")
        self.setTabToolTip(3, "Tab 3")
        
    def setTabContent(self, tab, content):
        layout = QVBoxLayout(tab)
        layout.addWidget(content)
        tab.setLayout(layout)

    def onTabChanged(self, index):
       # Lấy tên tab hiện tại
        current_tab_name = self.tabText(index)
        
        # Đặt lại tên ban đầu cho các tab không được chọn
        
        for i in range(1,self.count()):
            if i != index:
                self.setTabIcon(i, QIcon(self.tab_names[i]))

        # Đổi tên tab dựa trên index
        if index == 1:
            new_tab_name = "Device_white.png"
        elif index == 2:
            new_tab_name = "Device_white.png"
        elif index == 3:
            new_tab_name = "Device_white.png"
        else:
            new_tab_name = ""

        # Chỉ đổi tên nếu tên mới khác tên hiện tại
        if new_tab_name != current_tab_name:
            self.setTabIcon(index, QIcon(new_tab_name))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Side Menu Example")
        self.setGeometry(300, 300, 400, 300)

        # Tạo sidemenu
        side_menu = SideMenu()
        self.setCentralWidget(side_menu)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()