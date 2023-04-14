import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMessageBox, QLineEdit

from lab2.input_widget import InputWidget

from root import root
from math import sin


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Корни синуса")
        self.setMinimumSize(350, 400)
        self.move(600, 250)

        self.a = self.b = self.eps = None

        self.central_widget = QWidget()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

        # Input a
        self.layout.addWidget(QLabel('Введите значение a:'))
        self.layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='-10').connect(self.set_a))
        # Input b
        self.layout.addWidget(QLabel('Введите значение b:'))
        self.layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='10').connect(self.set_b))
        # Input eps
        self.layout.addWidget(QLabel('Введите значение eps:'))
        self.layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='0.001').connect(self.set_eps))
        # Calc button
        button = QPushButton('Вычисления')
        button.clicked.connect(self.clicked)
        self.layout.addWidget(button)
        # Output
        self.layout.addWidget(QLabel('Найденное значение корня:'))
        self.output_widget = QLineEdit(self.central_widget)
        self.output_widget.setReadOnly(True)
        self.layout.addWidget(self.output_widget)

        self.setCentralWidget(self.central_widget)

    def clicked(self):
        if self.a is None or isinstance(self.a, str):
            self.show_error(f'Некорректное значение a: {self.a}')
            return
        if self.b is None or isinstance(self.b, str):
            self.show_error(f'Некорректное значение b: {self.b}')
            return
        if self.eps is None or isinstance(self.eps, str):
            self.show_error(f'Некорректное значение eps: {self.eps}')
            return
        result = root(sin, self.a, self.b, self.eps)
        if result[0]:
            self.output_widget.setText('-')
            self.show_error('Невозможно найти корень')
        else:
            self.output_widget.setText(f'{result[1]:.6g}')

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_eps(self, eps):
        self.eps = eps

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
