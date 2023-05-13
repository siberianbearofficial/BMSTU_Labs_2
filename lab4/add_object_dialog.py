from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QLabel, QComboBox

from lab2.input_widget import InputWidget
from color import *

from styles import COMBO_BOX_STYLE, BIG_FONT


class AddObjectDialog(QDialog):
    def __init__(self, struct: dict):
        super().__init__()
        self.setWindowTitle("Добавление объекта")
        self.setMinimumWidth(240)

        self.setStyleSheet(f'background-color: {WHITE_COLOR};')

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.struct = dict()
        for field in struct:
            field_layout = QHBoxLayout()
            field_layout.setContentsMargins(0, 0, 0, 0)
            label = QLabel(field)
            label.setFont(BIG_FONT)
            field_layout.addWidget(label)

            if isinstance(struct[field], (float, int)):
                edit_widget = InputWidget(self, InputWidget.Float, str(struct[field]))
                edit_widget.setFont(BIG_FONT)
            else:
                raise NotImplementedError

            field_layout.addWidget(edit_widget)
            layout.addLayout(field_layout)
            self.struct[field] = edit_widget

        self.group = QComboBox()
        self.group.addItems(('1', '2'))
        self.group.setStyleSheet(COMBO_BOX_STYLE)
        self.group.setFont(BIG_FONT)
        self.group.get = lambda: int(self.group.currentText())
        label = QLabel('Группа')
        label.setFont(BIG_FONT)
        layout.addWidget(label)
        layout.addWidget(self.group)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
