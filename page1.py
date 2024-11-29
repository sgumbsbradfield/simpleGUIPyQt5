from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Page1(QWidget):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)

        # Set up the layout for Page1
        layout = QVBoxLayout(self)

        label = QLabel("Welcome to Page 1", self)
        label.setFont(font)

        button_back = QPushButton("Back to Home", self)
        button_back.setFont(font)
        button_back.clicked.connect(self.go_to_home)

        layout.addWidget(label)
        layout.addWidget(button_back)

    def go_to_home(self):
        """Emit a signal to return to the home page."""
        parent_widget = self.parentWidget()
        if isinstance(parent_widget, QStackedWidget):
            parent_widget.setCurrentIndex(0)  # Assuming home is the first page in QStackedWidget
