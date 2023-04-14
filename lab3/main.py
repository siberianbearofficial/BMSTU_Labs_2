import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QComboBox, QLabel, QWidget, QMessageBox, QApplication

from encoder_widgets import EncodeWidget, DecodeWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Стеганография")
        self.setMinimumSize(350, 300)
        self.move(600, 250)

        self.mode = 0

        self.central_widget = QWidget()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(QLabel('Режим работы'))
        self.mode_combo_box = QComboBox(self.central_widget)
        self.mode_combo_box.addItems(('Шифрование', 'Расшифровка'))
        self.mode_combo_box.currentIndexChanged.connect(self.set_mode)
        self.layout.addWidget(self.mode_combo_box)

        self.encode_widget = EncodeWidget(self.show_info, self.show_error)
        self.decode_widget = DecodeWidget(self.show_info, self.show_error)

        self.layout.addWidget(self.encode_widget)
        self.layout.addWidget(self.decode_widget)

        self.setCentralWidget(self.central_widget)
        self.update_layout()

    def set_mode(self, mode):
        self.mode = mode
        self.update_layout()

    def update_layout(self):
        if self.mode:
            self.encode_widget.hide()
            self.decode_widget.show()
        else:
            self.decode_widget.hide()
            self.encode_widget.show()

    def show_error(self, text):
        QMessageBox.warning(self, 'Внимание!', text, QMessageBox.Ok)

    def show_info(self, text):
        QMessageBox.information(self, 'Информация', text, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
