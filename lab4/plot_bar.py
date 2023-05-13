from PyQt5.QtWidgets import QWidget, QVBoxLayout

from plot import Plot
from color import *


class PlotBar(QWidget):
    def __init__(self, parent, get_objects=None, colors: dict = None, new_object=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        central_widget = QWidget()
        central_widget_layout = QVBoxLayout(central_widget)
        central_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.plot = Plot(get_objects, colors, new_object)

        central_widget_layout.addWidget(self.plot)
        layout.addWidget(central_widget)

        self.setStyleSheet(f'background-color: {PLOT_BG_COLOR}; border-radius: 10px;')
