from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Page2(QWidget):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)

        # Set up the layout for Page2
        layout = QVBoxLayout(self)

        label = QLabel("Welcome to Page 2", self)
        label.setFont(font)

        label1 = QLabel(self)
        image1 = QPixmap('image1.jpeg').scaled(2000, 200, QtCore.Qt.KeepAspectRatio)  # Resize to 200x200 while keeping aspect ratio
        label1.setPixmap(image1)

        label2 = QLabel(self)
        image2 = QPixmap('image2.jpg').scaled(2000, 200, QtCore.Qt.KeepAspectRatio)  # Resize to 200x200 while keeping aspect ratio
        label2.setPixmap(image2)

        button_back = QPushButton("Back to Home", self)
        button_back.setFont(font)
        button_back.clicked.connect(self.go_to_home)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(button_back)

    def go_to_home(self):
        """Emit a signal to return to the home page."""
        parent_widget = self.parentWidget()
        if isinstance(parent_widget, QStackedWidget):
            parent_widget.setCurrentIndex(0)  # Assuming home is the first page in QStackedWidget
