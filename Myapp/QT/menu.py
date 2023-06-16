from PySide6.QtGui import QPalette,QColor,QBrush,QScreen,QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea,QWidget,QHBoxLayout,QPushButton
from PySide6.QtCore import QObject, Signal,Qt
from ui.sidemenu import Delegate, SideMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        screen = QGuiApplication.primaryScreen()
        full_screen_size = screen.geometry()
        desktop_screen_size = screen.availableGeometry()
        self.width_screen_desktop = desktop_screen_size.width()
        self.height_screen_desktop = desktop_screen_size.height()
        self.width_screen_fullscreen = full_screen_size.width()
        self.height_screen_fullscreen = full_screen_size.height()
        self.setGeometry(0, 0, self.width_screen_desktop,
                         self.height_screen_desktop)
        # Tạo widget chính
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        # Tạo layout chính
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

   

        # Tạo SideMenu và widget bất kỳ
        self.side_menu = SideMenu()
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #f2f2f2;")
        
        # Thêm SideMenu và widget bất kỳ vào layout chính
        main_layout.addWidget(self.side_menu)
        main_layout.addWidget(content_widget)
        
    def handle_button_click(self):
        print("Button in Other clicked!")

    def showEvent(self, event):
        super(MainWindow, self).showEvent(event)
        self.side_menu.setFixedSize(40, self.height())
        self.side_menu.setMaximumHeight(self.height())
        


if __name__ == "__main__":
    import sys 

    app = QApplication([])
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())