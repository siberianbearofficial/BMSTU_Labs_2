from PyQt5.QtWidgets import QWidget, QVBoxLayout

from plot import Plot
from color import BG_COLOR


class PlotBar(QWidget):
    def __init__(self, parent, get_objects=None, colors: dict = None, new_object=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.plot = Plot(get_objects, colors, new_object)
        layout.addWidget(self.plot)

        self.setStyleSheet(f'background-color: {BG_COLOR}; border-radius: 10px;')
