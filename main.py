import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from page1 import Page1  # Import the Page1 class from the separate file
from page2 import Page2  # Import the Page2 class from the separate file


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)

        # Resize the window and set the title
        self.resize(2000, 500)
        self.setWindowTitle("PyQt5 - Main Window")

        # Create the layout
        self.layout = QVBoxLayout(self)

        # Create a QStackedWidget to hold multiple pages
        self.pages = QStackedWidget(self)
        self.layout.addWidget(self.pages)

        # Create the Home Page
        self.page_home = QWidget()
        self.pages.addWidget(self.page_home)

        # Add Pages from the imported module
        self.page1 = Page1()
        self.page2 = Page2()
        self.pages.addWidget(self.page1)
        self.pages.addWidget(self.page2)

        # Set up the Home Page
        self.setup_home_page(font)

        # Set the initial page to the Home Page
        self.pages.setCurrentWidget(self.page_home)

    def setup_home_page(self, font):
        """Set up the Home Page layout and widgets."""
        layout = QVBoxLayout(self.page_home)

        label = QLabel("Welcome to the Home Page", self.page_home)
        label.setFont(font)

        button_page1 = QPushButton("Page1", self.page_home)
        button_page1.setFont(font)
        button_page1.clicked.connect(self.go_to_page1)

        button_page2 = QPushButton("Page2", self.page_home)
        button_page2.setFont(font)
        button_page2.clicked.connect(self.go_to_page2)

        layout.addWidget(label)
        layout.addWidget(button_page1)
        layout.addWidget(button_page2)

    def go_to_page1(self):
        """Navigate to Page 1."""
        self.pages.setCurrentWidget(self.page1)

    def go_to_page2(self):
        """Navigate to Page 1."""
        self.pages.setCurrentWidget(self.page2)

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
