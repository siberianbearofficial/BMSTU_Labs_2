import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QApplication, \
    QPushButton, QMessageBox

from lab2.input_widget import InputWidget
from plot_bar import PlotBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Планиметрия")
        self.setMinimumSize(1080, 720)
        self.move(600, 250)

        self.central_widget = QWidget()

        self.layout = QHBoxLayout(self.central_widget)
        self.layout.setSpacing(10)

        self.input_layout = QVBoxLayout()
        self.input_layout.setAlignment(Qt.AlignTop)
        self.input_layout.addWidget(QLabel('Введите функцию:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Function, default='x**2 - 4'))
        self.input_layout.addWidget(QLabel('Введите значение a:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='-10'))
        self.input_layout.addWidget(QLabel('Введите значение b:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='10'))
        self.input_layout.addWidget(QLabel('Введите значение h:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.PositiveFloat, default='0.001'))
        self.input_layout.addWidget(QLabel('Введите значение Nmax:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Natural, default='1000'))
        self.input_layout.addWidget(QLabel('Введите значение eps:'))
        self.input_layout.addWidget(
            InputWidget(self.central_widget, InputWidget.Float, default='0.001'))
        button = QPushButton('Вычисления')
        button.clicked.connect(self.clicked)
        self.input_layout.addWidget(button)
        self.layout.addLayout(self.input_layout, 1)

        # Plot
        self.output_layout = QVBoxLayout()
        self.plot = PlotBar(self.central_widget)
        self.output_layout.addWidget(self.plot)
        self.layout.addLayout(self.output_layout, 2)

        self.setCentralWidget(self.central_widget)

    def clicked(self):
        pass

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
