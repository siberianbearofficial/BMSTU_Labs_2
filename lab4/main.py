"""
Лабораторная работа №4 "Планиметрия". Автор: Орлов Алексей (ИУ7-24Б).
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QApplication, \
    QPushButton, QMessageBox, QLabel

from angem import Point
from looper import Looper
from object_manager import ObjectManager
from inspector import Inspector
from plot_bar import PlotBar
from toolbar import ToolBar
from edit_object_dialog import EditObjectDialog
from add_object_dialog import AddObjectDialog
from clear_dialog import ClearDialog
from logic import *
from color import *
from styles import BUTTON_STYLE, BIG_FONT, LABEL_STYLE

P_SET_1 = 1
P_SET_2 = 2
TRIANGLE = 3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.om = ObjectManager()

        self.setWindowTitle("Планиметрия")
        self.setMinimumSize(1080, 720)
        self.move(600, 250)
        self.setStyleSheet(f'background-color: {BG_COLOR};')

        self.central_widget = QWidget()

        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setSpacing(10)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop)
        left_layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = ToolBar(
            {
                '1': (lambda: self.set_draw_mode(P_SET_1), True),
                '2': (lambda: self.set_draw_mode(P_SET_2), True),
                '+': (self.add_window, False),
                '🧹': (self.clear_window, False),
            }
        )

        self.calc_buttons = ToolBar(
            {
                'Один': (lambda: self.clicked_calc(True), False),
                'ВСЕ!': (self.clicked_calc, False),
            }
        )
        # self.button_calc = QPushButton('Построить!')
        # self.button_calc.setStyleSheet(BUTTON_STYLE)
        # self.button_calc.setFont(BIG_FONT)
        # self.button_calc.setMinimumHeight(50)
        # self.button_calc.clicked.connect(self.clicked_calc)

        self.inspector = Inspector(lambda item: self.om.select(item.id) if item else None, self.om.remove,
                                   lambda: self.om.edit(self.edit_window(list(self.om.get(selected=True))[0][0])))

        label = QLabel()
        label.setText('Точки')
        label.setFont(BIG_FONT)
        label.setStyleSheet(LABEL_STYLE)
        left_layout.addWidget(label)
        left_layout.addWidget(self.toolbar)
        # left_layout.addWidget(self.button_calc)

        label = QLabel()
        label.setText('Треугольники')
        label.setFont(BIG_FONT)
        label.setStyleSheet(LABEL_STYLE)
        left_layout.addWidget(label)
        left_layout.addWidget(self.calc_buttons)

        label = QLabel()
        label.setText('Список объектов')
        label.setFont(BIG_FONT)
        label.setStyleSheet(LABEL_STYLE)
        left_layout.addWidget(label)
        left_layout.addWidget(self.inspector)

        # Plot
        self.plot_bar = PlotBar(self.central_widget,
                                self.om.get,
                                {P_SET_1: RED_COLOR, P_SET_2: BLUE_COLOR},
                                lambda obj: self.om.add((obj, self.draw_mode)) if self.draw_mode else None)
        self.om.set_update_funcs(self.plot_bar.plot.update,
                                 lambda: self.inspector.update_items(self.om.get(every=True)))

        self.layout.addLayout(left_layout, 1)
        self.layout.addWidget(self.plot_bar, 3)
        self.setCentralWidget(self.central_widget)

        self.draw_mode = None
        self.dialog = None
        self.looper = None
        self.can_make_triangles = False

    def set_draw_mode(self, draw_mode):
        if draw_mode == self.draw_mode:
            self.draw_mode = None
        else:
            self.draw_mode = draw_mode

    def clicked_calc(self, only_first=False):
        self.can_make_triangles = False
        p_set_1 = list(self.om.group(P_SET_1))
        p_set_2 = list(self.om.group(P_SET_2))
        self.looper = Looper(lambda: find_triangle(p_set_1, p_set_2, only_first))
        self.looper.finished.connect(self.drawing_triangles_finished)
        self.looper.step.connect(self.draw_triangle)
        self.looper.start()

    def draw_triangle(self, triangle):
        self.om.add((triangle, TRIANGLE))
        self.can_make_triangles = True

    def drawing_triangles_finished(self):
        if not self.can_make_triangles:
            self.show_error('Невозможно построить требуемый треугольник')

    def show_error(self, text):
        QMessageBox.warning(None, 'Внимание!', text, QMessageBox.Ok)

    def edit_window(self, obj):
        try:
            self.dialog = EditObjectDialog(obj.__dict__)
        except NotImplementedError:
            return

        if self.dialog.exec():
            for field in self.dialog.struct:
                yield field, self.dialog.struct[field].get()

    def add_window(self):
        obj = Point(0, 0)
        try:
            self.dialog = AddObjectDialog(obj.__dict__)
        except NotImplementedError:
            return

        if self.dialog.exec():
            group = self.dialog.group.get()
            if group in (P_SET_1, P_SET_2):
                self.om.edit(((field, self.dialog.struct[field].get()) for field in self.dialog.struct), obj)
                self.om.add((obj, group))
            else:
                self.show_error('Нельзя добавить объект в эту группу!')

    def clear_window(self):
        self.dialog = ClearDialog()

        if self.dialog.exec():
            if not self.dialog.full_clear.get():
                self.om.clear()
            else:
                self.om.clear(TRIANGLE)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
