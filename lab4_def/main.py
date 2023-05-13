"""
Защита лабораторной работы №4 "Планиметрия". Автор: Орлов Алексей (ИУ7-24Б).
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QMessageBox

from object_manager import ObjectManager
from plot import Plot
from toolbar import ToolBar
from logic import *

POINT = 1
TRIANGLE = 2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.om = ObjectManager()

        self.setWindowTitle("Планиметрия")
        self.setMinimumSize(1080, 720)
        self.move(600, 250)

        self.central_widget = QWidget()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)

        self.toolbar = ToolBar(
            {
                'Решение!': (self.clicked_calc, False),
                '🧹': (self.om.clear, False),
            }
        )

        self.plot = Plot(self.om.get, lambda obj: self.om.add((obj, POINT)))
        self.om.set_update_func(self.plot.update)

        self.layout.addWidget(self.toolbar, 1)
        self.layout.addWidget(self.plot, 10)
        self.setCentralWidget(self.central_widget)

    def clicked_calc(self):
        triangle = find_triangle2(list(self.om.group(POINT)))
        if triangle:
            self.om.add((triangle, TRIANGLE))
        else:
            QMessageBox.warning(None, 'Внимание!', 'Невозможно построить требуемый треугольник', QMessageBox.Ok)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
