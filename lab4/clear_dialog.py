from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QLabel, QComboBox

from lab2.input_widget import InputWidget
from color import *

from styles import COMBO_BOX_STYLE, BIG_FONT


class ClearDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Очистка")
        self.setMinimumWidth(240)

        self.setStyleSheet(f'background-color: {WHITE_COLOR};')
        self.setFont(BIG_FONT)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        self.full_clear = QComboBox()
        self.full_clear.addItems(('Полная очистка', 'Только результат'))
        self.full_clear.setStyleSheet(COMBO_BOX_STYLE)
        self.full_clear.get = lambda: int(self.full_clear.currentIndex())
        layout.addWidget(self.full_clear)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
