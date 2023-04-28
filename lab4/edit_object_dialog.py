from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

from lab2.input_widget import InputWidget


class EditObjectDialog(QDialog):
    def __init__(self, struct: dict):
        super().__init__()
        self.setWindowTitle("Изменение объекта")
        self.setMinimumWidth(240)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.struct = dict()
        for field in struct:
            field_layout = QHBoxLayout()
            field_layout.setContentsMargins(0, 0, 0, 0)
            field_layout.addWidget(QLabel(field))

            if isinstance(struct[field], (float, int)):
                edit_widget = InputWidget(self, InputWidget.Float, str(struct[field]))
            else:
                raise NotImplementedError

            field_layout.addWidget(edit_widget)
            layout.addLayout(field_layout)
            self.struct[field] = edit_widget

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
