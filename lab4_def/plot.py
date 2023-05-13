from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget

import angem as ag


class Plot(QWidget):
    def __init__(self, get_objects, new_object):
        super().__init__()

        self.get_objects = get_objects
        self.new_object = new_object

        self.painter = QPainter()

    def paintEvent(self, e):
        self.painter.begin(self)
        for obj, _ in self.get_objects():
            self.draw(obj)
        self.painter.end()

    def mousePressEvent(self, a0):
        if a0.button() == 1:
            x, y = self.plot_x_to_ag_x(a0.pos().x()), self.plot_y_to_ag_y(a0.pos().y())
            self.new_object(ag.Point(x, y))
            self.update()

    def draw(self, obj, color=QColor(0, 0, 0)):
        self.painter.setPen(QPen(color, 3))
        brush = self.painter.brush()
        self.painter.setBrush(QColor(255, 255, 255))

        if isinstance(obj, ag.Point):
            self.painter.drawEllipse(int(self.ag_x_to_plot_x(obj.x) - 4),
                                     int(self.ag_y_to_plot_y(obj.y) - 4),
                                     8, 8)
        elif isinstance(obj, ag.Vector):
            self.painter.drawLine(int(self.ag_x_to_plot_x(obj.p1.x)), int(self.ag_y_to_plot_y(obj.p1.y)),
                                  int(self.ag_x_to_plot_x(obj.p2.x)), int(self.ag_y_to_plot_y(obj.p2.y)))
        elif isinstance(obj, ag.Triangle):
            self.draw(obj.v1, color)
            self.draw(obj.v2, color)
            self.draw(obj.v3, color)

        self.painter.setBrush(brush)

    def ag_x_to_plot_x(self, x):
        return self.width() // 2 + x

    def ag_y_to_plot_y(self, y):
        return self.height() // 2 - y

    def plot_x_to_ag_x(self, x):
        return x - self.width() // 2

    def plot_y_to_ag_y(self, y):
        return self.height() // 2 - y
