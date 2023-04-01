import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMessageBox

from input_widget import InputWidget
from plot_widget import PlotWidget
from table_widget import TableWidget

from root import roots, parse_func


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Анализ функции")
        self.setMinimumSize(1080, 720)
        self.move(600, 250)

        self.a = self.b = self.h = self.n_max = self.eps = self.func = None

        self.central_widget = QWidget()

        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setSpacing(10)

        self.input_layout = QVBoxLayout()
        self.input_layout.setAlignment(Qt.AlignTop)
        self.input_layout.addWidget(QLabel('Введите функцию:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Function, default='x**2 - 4').connect(self.set_func))
        self.input_layout.addWidget(QLabel('Введите значение a:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='-10').connect(self.set_a))
        self.input_layout.addWidget(QLabel('Введите значение b:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='10').connect(self.set_b))
        self.input_layout.addWidget(QLabel('Введите значение h:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.PositiveFloat, default='0.001').connect(self.set_h))
        self.input_layout.addWidget(QLabel('Введите значение Nmax:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Natural, default='1000').connect(self.set_n_max))
        self.input_layout.addWidget(QLabel('Введите значение eps:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='0.001').connect(self.set_eps))
        button = QPushButton('Вычисления')
        button.clicked.connect(self.clicked)
        self.input_layout.addWidget(button)
        self.layout.addLayout(self.input_layout, 1)

        self.output_layout = QVBoxLayout()
        self.plot = PlotWidget(self.central_widget)
        self.table = TableWidget(['[xi; xi+1]', 'x’', 'f(x’)', 'Кол-во итераций', 'Код ошибки'],
                                 self.central_widget)
        self.output_layout.addWidget(self.plot)
        self.output_layout.addWidget(self.table)
        self.output_layout.addWidget(QLabel(
            '0 - корень вычислен успешно;\n'
            '1 - произошло деление на ноль;\n'
            '2 - превышено максимальное число итераций;\n'
            '3 - найденный корень лежит за пределами отрезка [xi; xi+1].'))
        self.layout.addLayout(self.output_layout, 2)

        self.setCentralWidget(self.central_widget)

    def clicked(self):
        func_error, func, _, der_str = parse_func(self.func)
        if func_error:
            self.show_error(f'Некорректная функция: {str(self.func)}')
            return
        if self.a is None or isinstance(self.a, str):
            self.show_error(f'Некорректное значение a: {self.a}')
            return
        if self.b is None or isinstance(self.b, str):
            self.show_error(f'Некорректное значение b: {self.b}')
            return
        if self.h is None or isinstance(self.h, str):
            self.show_error(f'Некорректное значение h: {self.h}')
            return
        if self.n_max is None or isinstance(self.n_max, str):
            self.show_error(f'Некорректное значение Nmax: {self.n_max}')
            return
        if self.eps is None or isinstance(self.eps, str):
            self.show_error(f'Некорректное значение eps: {self.eps}')
            return
        self.table.clear()
        func_was_drawn = self.plot.draw_func(func, self.a, self.b, self.show_error)
        if func_was_drawn:
            found_roots = list()
            for r in self.get_roots():
                self.table.add_row(r)
                found_roots.append(r)
            self.plot.draw_points(func, found_roots, self.show_error, PlotWidget.RootsColor)
            self.plot.draw_points(func, list(self.get_roots(der_str)), self.show_error, PlotWidget.InflectionPointsColor)
            self.plot.legend(['Функция', 'Корни', 'Точки перегиба'])

    def set_func(self, func):
        self.func = func

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_h(self, h):
        self.h = h

    def set_n_max(self, n_max):
        self.n_max = n_max

    def set_eps(self, eps):
        self.eps = eps

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)

    def get_roots(self, func=None):
        for r in roots(func if func else self.func, self.h, [self.a, self.b], self.eps, self.n_max):
            yield r


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
