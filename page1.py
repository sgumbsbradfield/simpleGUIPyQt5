from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class Page1(QWidget):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)

        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)

        # List to store shapes positions
        self.shapes = []

        # Set up the layout for Page1
        layout = QVBoxLayout(self)

        label = QLabel("Welcome to Page 1", self)
        label.setFont(font)

        button_ellipse = QPushButton("Draw Ellipse", self)
        button_ellipse.setFont(font)
        button_ellipse.clicked.connect(lambda: self.draw_random_shape("ellipse"))

        button_square = QPushButton("Draw Square", self)
        button_square.setFont(font)
        button_square.clicked.connect(lambda: self.draw_random_shape("square"))

        button_rect = QPushButton("Draw Rect", self)
        button_rect.setFont(font)
        button_rect.clicked.connect(lambda: self.draw_random_shape("rect"))

        button_clear = QPushButton("Clear All Shapes", self)
        button_clear.setFont(font)
        button_clear.clicked.connect(self.clear_shapes)

        button_back = QPushButton("Back to Home", self)
        button_back.setFont(font)
        button_back.clicked.connect(self.go_to_home)

        layout.addWidget(label)
        layout.addWidget(button_ellipse)
        layout.addWidget(button_square)
        layout.addWidget(button_rect)
        layout.addWidget(button_clear)
        layout.addWidget(button_back)

        self.setLayout(layout)

    def draw_random_shape(self, shapeType):
        """Generate a random position for a new ellipse and trigger a repaint."""
        # Generate random position and size for the ellipse
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colour = QColor(red, green, blue)
        shape = (
            shapeType,
            random.randint(50, self.width() - 100),  # X-coordinate
            random.randint(200, self.height() - 100),  # Y-coordinate
            random.randint(50, 150),  # Width
            random.randint(50, 150), # Height
            colour #Colour
        )
        self.shapes.append(shape)  # Add the new ellipse to the list
        self.update()  # Trigger the paintEvent to redraw the widget

    def clear_shapes(self):
        """Clear all ellipses and repaint."""
        self.shapes = []  # Clear the list of shapes
        self.update()  # Trigger the paintEvent to repaint the widget

    def mousePressEvent(self, event):
        """Draw an ellipse at the position where the mouse is clicked."""
        if event.button() == Qt.LeftButton:  # Only handle left mouse button clicks
            shapeType = random.choice(["ellipse","square","rect"])
            x = event.x() - random.randint(50, 150)  # Center the ellipse around the click
            y = event.y() - random.randint(50, 150)  # Center the ellipse around the click
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colour = QColor(red, green, blue)

            shape = (shapeType, x, y, random.randint(50, 150), random.randint(50, 150), colour)  # Fixed size of 50x50 for the ellipse

            self.shapes.append(shape)
            self.update()  # Trigger a repaint

    def paintEvent(self, event):
        """Override paintEvent to draw all ellipses."""
        super(Page1, self).paintEvent(event)
        painter = QPainter(self)

        painter.setPen(Qt.NoPen)  # Remove border
        for shape in self.shapes:
            type, x, y, w, h, c = shape
            painter.setBrush(QBrush(c, Qt.SolidPattern))  # Set fill color
            if type == 'ellipse':
                painter.drawEllipse(x, y, w, h)
            elif type == 'square':
                painter.drawRect(x, y, w, w)
            elif type == 'rect':
                painter.drawRect(x, y, w, h)
                painter.draw

    def go_to_home(self):
        """Emit a signal to return to the home page."""
        parent_widget = self.parentWidget()
        if isinstance(parent_widget, QStackedWidget):
            parent_widget.setCurrentIndex(0)  # Assuming home is the first page in QStackedWidget
