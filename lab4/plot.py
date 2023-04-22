from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget

from axis import Axis
from color import BLACK_COLOR, BG_COLOR

import angem as ag

THICKNESS = 3
RADIUS = 4


class Plot(QWidget):
    def __init__(self):
        super().__init__()

        p1 = ag.Point(50, 100)
        p2 = ag.Point(300, 20)

        self.painter = QPainter()

        self.axis_x = ag.Segment(ag.Point(-self.width(), 0), ag.Point(self.width(), 0))
        self.axis_y = ag.Segment(ag.Point(0, -self.height()), ag.Point(0, self.height()))

        self.objects = [p1, p2]

    def paintEvent(self, e):
        self.painter.begin(self)

        # Drawing axis x and axis y
        self.draw(self.axis_x)
        self.draw(self.axis_y)

        for obj in self.objects:
            self.draw(obj)

        # if self.selected_object_index:
        #     self.selected_object.draw(selected=1)

        self.painter.end()

    def draw(self, obj, color=BLACK_COLOR):
        self.set_pen(color, THICKNESS)
        brush = self.painter.brush()
        self.painter.setBrush(BG_COLOR)

        if isinstance(obj, ag.Point):
            self.painter.drawEllipse(int(self.ag_x_to_plot_x(obj.x) - RADIUS),
                                     int(self.ag_y_to_plot_y(obj.y) - RADIUS),
                                     RADIUS * 2, RADIUS * 2)
        elif isinstance(obj, ag.Segment):
            self.painter.drawLine(int(self.ag_x_to_plot_x(obj.p1.x)), int(self.ag_y_to_plot_y(obj.p1.y)),
                                  int(self.ag_x_to_plot_x(obj.p2.x)), int(self.ag_y_to_plot_y(obj.p2.y)))
            self.draw(obj.p1, color)
            self.draw(obj.p2, color)
        elif isinstance(obj, ag.Line):
            p1 = obj.p - obj.v.norm() * self.width() * self.height()
            p2 = obj.p + obj.v.norm() * self.width() * self.height()
            self.painter.drawLine(int(self.ag_x_to_plot_x(p1.x)), int(self.ag_y_to_plot_y(p1.y)),
                                  int(self.ag_x_to_plot_x(p2.x)), int(self.ag_y_to_plot_y(p2.y)))

        self.painter.setBrush(brush)

    def ag_x_to_plot_x(self, x):
        return self.width() // 2 + x

    def ag_y_to_plot_y(self, y):
        return self.height() // 2 - y

    def set_pen(self, color, thickness, line_type=1):
        self.painter.setPen(QPen(color, int(thickness), line_type))

    def clear(self):
        self.objects.clear()
        self.update()

    def update(self, selected=0) -> None:
        # self.selected_mode = selected
        super().update()
