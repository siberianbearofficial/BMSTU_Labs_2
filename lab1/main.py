"""
Автор: Орлов Алексей (Группа: ИУ7-24Б)
Сложение, вычитание и умножение вещественных чисел в 2-й системе
счисления.
"""

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget,
    QLineEdit,
    QComboBox,
    QMessageBox,
    QAction,
    QMenuBar
)

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMouseEvent

from binary_arithmetic.binary_arithmetic_strings import bin_sum, bin_sub, bin_mul

import sys


class Keyboard(QHBoxLayout):
    def __init__(self, *names, btn_height=50):
        super().__init__()

        self.btn_height = btn_height

        self.buttons = list()
        for name in names:
            btn = QPushButton(name)
            btn.setFixedHeight(self.btn_height)
            self.addWidget(btn)
            self.buttons.append(btn)

    def connect(self, *connectors):
        if len(connectors) != len(self.buttons):
            raise ValueError('Not enough values to unpack.')
        for i in range(len(self.buttons)):
            self.buttons[i].clicked.connect(connectors[i])
        return self


class OperandWidget(QLineEdit):
    def __init__(self, height, text_size):
        super().__init__()

        font = self.font()
        font.setPointSize(text_size)
        self.setFont(font)
        self.setFixedHeight(height)
        self.setClearButtonEnabled(True)

        self.textChanged.connect(self.on_text_changed)
        self.clicked_listener = None

    def add(self, text):
        self.setText(self.text() + text)

    def on_text_changed(self):
        filtered_text = list()
        for sym in self.text():
            if sym in '01':
                filtered_text.append(sym)
            elif sym == '-' and not filtered_text:
                filtered_text.append('-')
            elif sym in '.,' and '.' not in filtered_text:
                if not filtered_text:
                    filtered_text.append('0')
                filtered_text.append('.')
        self.setText(''.join(filtered_text))

    def set_on_clicked_listener(self, clicked_listener):
        self.clicked_listener = clicked_listener

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if self.clicked_listener:
            self.clicked_listener()


class OutputWidget(QLabel):
    def __init__(self, width, height, text_size):
        super().__init__()

        font = self.font()
        font.setPointSize(text_size)
        self.setFont(font)
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.setStyleSheet('background-color: white; border: 1px solid blue;')
        self.setContentsMargins(3, 0, 3, 0)


class OperationWidget(QComboBox):
    def __init__(self, height):
        super().__init__()

        self.operation = bin_sum

        self.setFixedHeight(height)
        self.addItems(["+", "-", "*"])

        font = self.font()
        font.setPointSize(height // 2)
        self.setFont(font)

        self.currentIndexChanged.connect(self.operation_changed)

    def operation_changed(self, index):
        self.operation = (bin_sum, bin_sub, bin_mul)[index]


class OperationLine(QHBoxLayout):
    def __init__(self, width, height):
        super().__init__()

        self.operand1 = OperandWidget(height, height // 2)
        self.operand2 = OperandWidget(height, height // 2)
        self.operation = OperationWidget(height)
        self.output_line = OutputWidget(round(width * 0.5), height, height // 2)

        self.selected = self.operand1

        self.operand1.set_on_clicked_listener(lambda: self.select(self.operand1))
        self.operand2.set_on_clicked_listener(lambda: self.select(self.operand2))

        self.addWidget(self.operand1)
        self.addWidget(self.operation)
        self.addWidget(self.operand2)
        self.addWidget(self.output_line)

    def select(self, selected):
        self.selected = selected

    def add_0(self):
        self.selected.add('0')

    def add_1(self):
        self.selected.add('1')

    def add_p(self):
        self.selected.add('.')

    def add_m(self):
        self.selected.add('-')

    def backspace(self):
        self.selected.backspace()

    def clear(self):
        self.operand1.clear()
        self.operand2.clear()
        self.output_line.clear()

    def calculate(self):
        if self.operand1.text() and self.operand2.text():
            arg1 = self.operand1.text()
            arg2 = self.operand2.text()
            operation = self.operation.operation

            res = operation(arg1, arg2)
            self.output_line.setText(res)


class Menubar(QMenuBar):
    def __init__(self, *names):
        super().__init__()

        for name in names:
            self.addAction(QAction('&{}'.format(name), self))

    def connect(self, *funcs):
        actions = self.actions()
        if len(funcs) != len(actions):
            return

        for i in range(len(funcs)):
            actions[i].triggered.connect(funcs[i])

        return self


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Сложение, вычитание и умножение в 2-й сс")
        self.setFixedSize(QSize(1920, 200))
        self.move(0, 0)

        self.operations = OperationLine(self.width(), 50)
        self.buttons = Keyboard('0', '1', '.', '-', '=', '<-', 'C').connect(self.operations.add_0,
                                                                            self.operations.add_1,
                                                                            self.operations.add_p,
                                                                            self.operations.add_m,
                                                                            self.operations.calculate,
                                                                            self.operations.backspace,
                                                                            self.operations.clear)
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.operations)
        self.layout.addLayout(self.buttons)
        self.setLayout(self.layout)

        menubar = Menubar('Информация', 'Вычислить', 'Очистить поле 1', 'Очистить поле 2', 'Очистить все').connect(
            self.show_author_info,
            self.operations.calculate,
            self.operations.operand1.clear,
            self.operations.operand2.clear,
            self.operations.clear)

        self.setMenuBar(menubar)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def show_author_info(self):
        title = 'Информация об авторе и назначении программы'
        author_info = 'Автор: Орлов Алексей (Группа: ИУ7-24Б)\nСложение, вычитание и умножение вещественных чисел в ' \
                      '2-й системе счисления. '
        QMessageBox.information(self, title, author_info, QMessageBox.Ok)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
