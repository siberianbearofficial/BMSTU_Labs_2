import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMessageBox, QLineEdit, QDoubleSpinBox

from root import root
from math import sin


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Корни синуса")
        self.setMinimumSize(350, 400)
        self.move(600, 250)

        self.central_widget = QWidget()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

        # Input a
        self.layout.addWidget(QLabel('Введите значение a:'))
        a = QDoubleSpinBox()
        a.setRange(-1000000, 1000000)
        a.setValue(-1)
        a.valueChanged.connect(self.set_a)
        self.layout.addWidget(a)
        # Input b
        self.layout.addWidget(QLabel('Введите значение b:'))
        b = QDoubleSpinBox()
        b.setRange(-1000000, 1000000)
        b.setValue(1)
        b.valueChanged.connect(self.set_b)
        self.layout.addWidget(b)
        # Input eps
        self.layout.addWidget(QLabel('Введите значение eps:'))
        eps = QDoubleSpinBox()
        eps.setRange(0.000001, 1000000)
        eps.setDecimals(6)
        eps.setValue(0.000001)
        eps.valueChanged.connect(self.set_eps)
        self.layout.addWidget(eps)
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

        self.a, self.b, self.eps = a.value(), b.value(), eps.value()

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
