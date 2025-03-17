import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QEvent

class HoverMouseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(150, 150, 500, 500)
        self.setWindowTitle("Tugas 2 - Muhammad Ridho Fahru Rozy - F1D0222076")

        self.coord_label = QLabel("x:(0), y:(0)", self)
        self.coord_label.setStyleSheet("""
            font-size: 16px;
            color: black;
            background-color: white;
            padding: 6px;
            border-radius: 8px;
        """)
        self.coord_label.setMinimumSize(120, 35)
        self.coord_label.move(30, 30)
        self.setMouseTracking(True)
        
        self.coord_label.installEventFilter(self)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        self.coord_label.setText(f"x:({x}), y:({y})")
        self.coord_label.adjustSize()

    def eventFilter(self, obj, event):
        if obj == self.coord_label and event.type() == QEvent.Enter:
            max_x = self.width() - self.coord_label.width()
            max_y = self.height() - self.coord_label.height()
            new_x = random.randint(0, max_x)
            new_y = random.randint(0, max_y)
            self.coord_label.move(new_x, new_y)
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HoverMouseApp()
    main_window.show()
    sys.exit(app.exec_())
