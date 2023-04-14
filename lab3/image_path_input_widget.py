from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog


class ImagePathInputWidget(QWidget):
    SAVE_MODE = 0
    OPEN_MODE = 1

    def __init__(self, mode, on_selected):
        super().__init__()

        self.mode = mode
        self.on_selected = on_selected

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.image_path = QLineEdit()
        self.image_path.setReadOnly(True)
        self.layout.addWidget(self.image_path)

        self.select_button = QPushButton('Обзор')
        self.select_button.clicked.connect(self.clicked)
        self.layout.addWidget(self.select_button)

    def clicked(self):
        match self.mode:
            case ImagePathInputWidget.SAVE_MODE:
                path = QFileDialog.getSaveFileName(filter='Images (*.bmp)')
            case ImagePathInputWidget.OPEN_MODE:
                path = QFileDialog.getOpenFileName(filter='Images (*.bmp)')
            case _:
                raise ValueError(f'Mode {self.mode} is not supported')
        if path and path[0]:
            if not path[0].endswith('.bmp'):
                self.image_path.setText(path[0] + '.bmp')
                self.on_selected(path[0] + '.bmp')
            else:
                self.image_path.setText(path[0])
                self.on_selected(path[0])
