from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class PlotWidget(QWidget):
    RootsColor = None
    InflectionPointsColor = None

    def __init__(self, parent=None):
        if parent:
            super().__init__(parent)
        else:
            super().__init__()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.draw_func(lambda x: x ** 2, -10, 10)
        self.ax = None

    def clear(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

    def draw_func(self, func, a, b, error_stream=None):
        try:
            x = [a]
            y = [func(a)]
            step = (b - a) / 1000
            while x[-1] < b + step / 2:
                x.append(x[-1] + step)
                y.append(func(x[-1] + step))

            self.clear()
            self.ax.plot(x, y)
            self.canvas.draw()
            return True
        except Exception as ex:
            msg = f'Невозможно построить график на этом интервале: {ex.__class__.__name__}: {ex}'
            error_stream(msg) if error_stream else print(msg)
            return False

    def draw_points(self, func, der, error_stream=None, color=None):
        if not color:
            color = PlotWidget.RootsColor
        try:
            x_list = list()
            y_list = list()
            for code, _, __, x, ___ in der:
                if not code:
                    x_list.append(x)
                    y_list.append(func(x))
            self.ax.scatter(x_list, y_list, color=color)
            self.canvas.draw()
            return True
        except Exception as ex:
            msg = f'Невозможно построить точки перегиба на этом интервале: {ex.__class__.__name__}: {ex}'
            error_stream(msg) if error_stream else print(msg)
            return False

    def legend(self, args):
        self.ax.legend(args, loc='lower left')
        self.canvas.draw()
