from PySide6.QtCore import Qt, QAbstractListModel, QSize, QRect, QEvent,QTimer,QModelIndex,Signal,QObject
from PySide6.QtGui import QPainter, QPixmap, QFont, QColor, QMouseEvent
from PySide6.QtWidgets import (
    QMdiSubWindow, QWidget, QGraphicsDropShadowEffect, QStyleOption, QStyle,
    QVBoxLayout, QListView, QFrame, QStyledItemDelegate, QLabel, QToolTip,QPushButton
)

class Delegate(QStyledItemDelegate):
    def __init__(self, height=None):
        super(Delegate, self).__init__()
        if height is None:
            self._height = 45
        else:
            self._height = height
        self._hovered_index = None
        self._selected_index = None
        self.hello = None

    def paint(self, painter, option, index):
        widget = option.widget
        if widget is not None:
            widget.setMouseTracking(True)

        super(Delegate, self).paint(painter, option, index)
        
        if index.row() == self._selected_index:
            icon_path = index.data()[2]
        else:
            icon_path = index.data()[1]
        icon = QPixmap()
        icon.load(icon_path)
        icon = icon.scaled(24, 24, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        left = 5  # margin left
        icon_pos = QRect(left, ((self._height - icon.height()) / 2) + option.rect.y(), icon.width(), icon.height())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(icon_pos, icon)
    

    
    def helpEvent(self, event, view, option, index):
        if event.type() == QEvent.ToolTip:
            tooltip_text = index.data(Qt.ToolTipRole)
            QToolTip.showText(event.pos(), tooltip_text) 
        return super().helpEvent(event, view, option, index)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonPress:
            
            self._selected_index = index.row()  # Cập nhật _selected_index với chỉ số hàng của mục được chọn
            option.widget.viewport().update()  # Cập nhật giao diện để vẽ lại tất cả các mục
        return super().editorEvent(event, model, option, index)
    


    def sizeHint(self, option, index):
        return QSize(0, self._height)


class Model(QAbstractListModel):
    def __init__(self, data=None):
        super(Model, self).__init__()
        if data is None:
            data = [
                ("Streaming", "res/img/icons/Streaming_white.png","res/img/icons/Streaming_red.png"),
                ("Playback", "res/img/icons/Playback_white.png","res/img/icons/Playback_red.png"),
                ("Device Management", "res/img/icons/Device_white.png","res/img/icons/Device_red.png"),
                ("Map", "res/img/icons/Map_white.png","res/img/icons/Map_red.png"),
                ("User Management", "res/img/icons/User_white.png","res/img/icons/User_red.png"),
                ("Setting", "res/img/icons/Gear_white.png","res/img/icons/Gear_red.png"),
            ]
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):   
        if index.isValid():
            if role == Qt.DisplayRole:
                return self._data[index.row()]
            elif role == Qt.ToolTipRole:
                return self._data[index.row()][0]

        return None



class ListView(QListView):
    def __init__(self):
        super(ListView, self).__init__()
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        # CHANGE CURSOR HOVERING
        if self.indexAt(event.pos()).row() >= 0:
            self.setCursor(Qt.PointingHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor)


class Profile(QWidget):
    def __init__(self, height=None):
        super(Profile, self).__init__()
        if height is None:
            self.setFixedHeight(150)
        else:
            self.setFixedHeight(height)
        self.paintAvatar()

    def paintAvatar(self):
        # CREATE LAYOUT
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)
        # BACKGROUND IMAGE
        image_label = QLabel(self)
        image_label.setPixmap(QPixmap("res/img/icons/Logo.png"))
        image_label.setScaledContents(True)  # Kích thước ảnh tự động điều chỉnh
        layout.addWidget(image_label)

        # SET LAYOUT
        self.setLayout(layout)


class SideMenuWidget(QWidget):
    def __init__(self):
        super(SideMenuWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        # self.layout.setSpacing(12)
        self.setLayout(self.layout)

        # PROFILE
        self.layout.addWidget(Profile(height=80))
        
        
        # BUTTONS
        self.listview = ListView()
        self.listview.setMouseTracking(True)
        self.listview.setFrameStyle(QFrame.NoFrame)
        self.listview.setFocusPolicy(Qt.NoFocus)
        self.listview.setModel(Model())
        self.listview.setItemDelegate(Delegate())
        
        self.layout.addWidget(self.listview)
        self.setStyleSheet("background: #1C2039;")

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)


class SideMenu(QMdiSubWindow):
    def __init__(self):
        super(SideMenu, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(50)
        self.setGraphicsEffect(self.shadow)
        self.widget = SideMenuWidget()
        self.setWidget(self.widget)
        
