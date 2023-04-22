import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox, QApplication

from invert_widget import InvertWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window properties
        self.setWindowTitle("Инвертирование")
        self.setMinimumSize(350, 150)
        self.move(600, 250)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

        # Invert widget
        self.invert_widget = InvertWidget(self.show_info, self.show_error)
        self.layout.addWidget(self.invert_widget)

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)

    def show_info(self, text):
        QMessageBox.information(self, 'Информация', text, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
