from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

from image_path_input_widget import ImagePathInputWidget

import encoder as enc


class EncodeWidget(QWidget):
    def __init__(self, success_stream=print, error_stream=print):
        super().__init__()

        self.input_image_path = ''
        self.output_image_path = ''
        self.error_stream = error_stream
        self.success_stream = success_stream

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(QLabel('Выберите изображение для зашифровки'))
        self.image_input = ImagePathInputWidget(ImagePathInputWidget.OPEN_MODE, self.set_input_image_path)
        self.layout.addWidget(self.image_input)

        self.layout.addWidget(QLabel('Строка для зашифровки'))
        self.encode_string = QLineEdit()
        self.layout.addWidget(self.encode_string)

        self.layout.addWidget(QLabel('Выберите, куда сохранить зашифрованное изображение'))
        self.image_output = ImagePathInputWidget(ImagePathInputWidget.SAVE_MODE, self.set_output_image_path)
        self.layout.addWidget(self.image_output)

        self.encode_button = QPushButton('Зашифровать')
        self.encode_button.clicked.connect(self.encode)
        self.layout.addWidget(self.encode_button)

    def encode(self):
        if self.input_image_path and self.output_image_path and self.encode_string.text():
            try:
                img = Image.open(self.input_image_path)
                enc.encode(img.load(), img.size, self.encode_string.text())
                img.save(self.output_image_path)
                self.success_stream('Изображение успешно зашифровано')
            except Exception as e:
                self.error_stream(str(e))
        else:
            self.error_stream('Невозможно выполнить шифрование')

    def set_input_image_path(self, path):
        if path:
            self.input_image_path = path

    def set_output_image_path(self, path):
        if path:
            self.output_image_path = path


class DecodeWidget(QWidget):
    def __init__(self, success_stream=print, error_stream=print):
        super().__init__()

        self.image_path = ''
        self.error_stream = error_stream
        self.success_stream = success_stream

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignTop)

        self.layout.addWidget(QLabel('Выберите изображение для расшифровки'))
        self.image_input = ImagePathInputWidget(ImagePathInputWidget.OPEN_MODE, self.set_image_path)
        self.layout.addWidget(self.image_input)

        self.layout.addWidget(QLabel('Результат расшифровки'))
        self.decode_result = QLineEdit()
        self.decode_result.setReadOnly(True)
        self.layout.addWidget(self.decode_result)

        self.decode_button = QPushButton('Расшифровать')
        self.decode_button.clicked.connect(self.decode)
        self.layout.addWidget(self.decode_button)

    def set_image_path(self, path):
        if path:
            self.image_path = path

    def decode(self):
        if self.image_path:
            try:
                img = Image.open(self.image_path)
                res = enc.decode(img.load(), img.size)
                self.decode_result.setText(res)
                self.success_stream('Изображение успешно расшифровано')
            except Exception as e:
                self.decode_result.setText('')
                self.error_stream(f'Ошибка: {e}')
        else:
            self.error_stream('Невозможно выполнить расшифровку')
