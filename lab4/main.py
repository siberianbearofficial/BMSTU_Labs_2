import sys
from time import sleep

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMessageBox, QDialog, QDialogButtonBox, QLineEdit

from lab4.looper import Looper
from object_manager import ObjectManager
from inspector import Inspector
from plot_bar import PlotBar
from edit_object_dialog import EditObjectDialog
from logic import *
from color import BLUE_COLOR, RED_COLOR

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

        self.central_widget = QWidget()

        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setSpacing(10)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop)
        left_layout.setContentsMargins(0, 0, 0, 0)

        button1 = QPushButton('1')
        button1.clicked.connect(lambda: self.set_draw_mode(P_SET_1))
        button2 = QPushButton('2')
        button2.clicked.connect(lambda: self.set_draw_mode(P_SET_2))

        button_clear = QPushButton('Очистить')
        button_clear.clicked.connect(self.om.clear)

        self.button_calc = QPushButton('Треугольник')
        self.button_calc.clicked.connect(self.clicked_calc)

        self.inspector = Inspector(lambda item: self.om.select(item.id) if item else None, self.om.remove,
                                   lambda: self.om.edit(self.edit_window(list(self.om.get(selected=True))[0][0])))

        left_layout.addWidget(button1)
        left_layout.addWidget(button2)
        left_layout.addWidget(self.button_calc)
        left_layout.addWidget(button_clear)
        left_layout.addWidget(self.inspector)

        # Plot
        self.plot_bar = PlotBar(self.central_widget,
                                self.om.get,
                                {P_SET_1: RED_COLOR, P_SET_2: BLUE_COLOR},
                                lambda obj: self.om.add((obj, self.draw_mode)))
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
        self.draw_mode = draw_mode

    def clicked_calc(self):
        self.button_calc.setDisabled(True)
        self.can_make_triangles = False
        p_set_1 = list(self.om.group(P_SET_1))
        p_set_2 = list(self.om.group(P_SET_2))
        self.looper = Looper(lambda: find_triangle(p_set_1, p_set_2))
        self.looper.finished.connect(self.drawing_triangles_finished)
        self.looper.step.connect(self.draw_triangle)
        self.looper.start()

    def draw_triangle(self, triangle):
        self.om.add((triangle, TRIANGLE))
        self.can_make_triangles = True

    def drawing_triangles_finished(self):
        self.button_calc.setDisabled(False)
        if not self.can_make_triangles:
            self.show_error('Невозможно построить требуемый треугольник')

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)

    def edit_window(self, obj):
        try:
            self.dialog = EditObjectDialog(obj.__dict__)
        except NotImplementedError:
            return

        if self.dialog.exec():
            for field in self.dialog.struct:
                yield field, self.dialog.struct[field].get()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
