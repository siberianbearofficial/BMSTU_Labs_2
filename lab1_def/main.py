from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QMessageBox,
    QLabel
)

import sys

from fib_to_10 import fib_to_10


class InputLine(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(80)
        font = self.font()
        font.setPointSize(50)
        self.setFont(font)

        self.textChanged.connect(self.text_changed)

    def text_changed(self):
        new_text = list()
        first_zero = True
        last_one = False
        for sym in self.text():
            if sym == '1' and not last_one:
                first_zero = False
                last_one = True
                new_text.append('1')
            elif sym == '0' and not first_zero:
                new_text.append('0')
                last_one = False
        self.setText(''.join(new_text))


class OutputLine(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setMinimumHeight(80)
        self.setReadOnly(True)
        font = self.font()
        font.setPointSize(50)
        self.setFont(font)


class CalculationButton(QPushButton):
    def __init__(self):
        super().__init__('Перевести')

        self.setMinimumHeight(80)
        font = self.font()
        font.setPointSize(25)
        self.setFont(font)

    def set_on_click_listener(self, func):
        if func:
            self.clicked.connect(func)
        return self


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Перевод из фибоначчиевой сс в 10 сс")
        self.setBaseSize(720, 480)
        self.move(600, 250)

        self.label1 = InputLine()
        self.label2 = OutputLine()
        self.btn = CalculationButton().set_on_click_listener(self.calculate)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Введите число:'))
        self.layout.addWidget(self.label1)
        self.layout.addWidget(QLabel('Результат:'))
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def calculate(self):
        res = fib_to_10(self.label1.text())
        if res:
            self.label2.setText(str(res))
        else:
            QMessageBox.warning(self, 'Некорректный ввод', 'Повторите ввод заново', QMessageBox.Ok)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
