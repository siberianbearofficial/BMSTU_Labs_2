from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from image_path_input_widget import ImagePathInputWidget as ipiw

import inverter as inv


class InvertWidget(QWidget):
    def __init__(self, success_stream=print, error_stream=print):
        super().__init__()

        self.input_image_path = ''
        self.error_stream = error_stream
        self.success_stream = success_stream

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignTop)

        # Input image
        self.layout.addWidget(QLabel('Выберите изображение для инвертирования'))
        self.image_input = ipiw(ipiw.OPEN_MODE, self.set_input_image_path)
        self.layout.addWidget(self.image_input)

        # Invert button
        self.invert_button = QPushButton('Инвертировать')
        self.invert_button.clicked.connect(self.invert)
        self.layout.addWidget(self.invert_button)

    def invert(self):
        output_image_path = ipiw.ensure_bmp(ipiw.get_file_name(ipiw.SAVE_MODE))
        if self.input_image_path and output_image_path:
            try:
                img = Image.open(self.input_image_path)
                inv.invert(img.load(), img.size)
                img.save(output_image_path)
                self.success_stream('Изображение успешно инвертировано')
            except ValueError as e:
                self.error_stream(str(e))
            except Exception as e:
                self.error_stream(f'Неизвестная ошибка: {e}')
        else:
            self.error_stream('Невозможно выполнить инвертирование')

    def set_input_image_path(self, path):
        if path:
            self.input_image_path = path

    def set_output_image_path(self, path):
        if path:
            self.output_image_path = path
