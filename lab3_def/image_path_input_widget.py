from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog

from os.path import basename


class ImagePathInputWidget(QWidget):
    SAVE_MODE = 0
    OPEN_MODE = 1

    def __init__(self, mode, on_selected):
        super().__init__()

        self.mode = mode
        self.on_selected = on_selected

        # Layout
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Image path
        self.image_path = QLineEdit()
        self.image_path.setReadOnly(True)
        self.layout.addWidget(self.image_path)

        # Select button
        self.select_button = QPushButton('Обзор')
        self.select_button.clicked.connect(self.clicked)
        self.layout.addWidget(self.select_button)

    def clicked(self):
        path = ImagePathInputWidget.get_file_name(self.mode)
        if path:
            path = ImagePathInputWidget.ensure_bmp(path)
            self.image_path.setText(basename(path))
            self.on_selected(path)

    @staticmethod
    def get_file_name(mode):
        match mode:
            case ImagePathInputWidget.SAVE_MODE:
                path = QFileDialog.getSaveFileName(filter='Images (*.bmp)')
            case ImagePathInputWidget.OPEN_MODE:
                path = QFileDialog.getOpenFileName(filter='Images (*.bmp)')
            case _:
                raise ValueError(f'Mode {mode} is not supported')
        if path and path[0]:
            return path[0]
        return None

    @staticmethod
    def ensure_bmp(path):
        if not path.endswith('.bmp'):
            return path + '.bmp'
        return path
