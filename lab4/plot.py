from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget

from color import *

import angem as ag

THICKNESS = 3
RADIUS = 4


class Plot(QWidget):
    def __init__(self, get_objects=None, colors: dict = None, new_object=None):
        super().__init__()

        self.get_objects = get_objects
        self.new_object = new_object
        self.group_colors = colors if colors else dict()

        self.painter = QPainter()

        self.axis_x = ag.Line(ag.Point(0, 0), ag.Point(1, 0))
        self.axis_y = ag.Line(ag.Point(0, 0), ag.Point(0, 1))

    def paintEvent(self, e):
        self.painter.begin(self)

        # Drawing axis x and axis y
        self.draw(self.axis_x)
        self.draw(self.axis_y)

        if self.get_objects:
            for obj, group in self.get_objects():
                self.draw(obj, self.group_colors.get(group, BLACK_COLOR))
            for obj, _ in self.get_objects(selected=True):
                if obj:
                    self.draw(obj, SELECTED_COLOR)

        self.painter.end()

    def mousePressEvent(self, a0):
        if a0.button() == 1 and self.new_object:
            x, y = self.plot_x_to_ag_x(a0.pos().x()), self.plot_y_to_ag_y(a0.pos().y())
            self.new_object(ag.Point(x, y))
            self.update()

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
            # self.draw(obj.p1, color)
            # self.draw(obj.p2, color)
        elif isinstance(obj, ag.Line):
            try:
                p1 = int(self.ag_x_to_plot_x(obj.x(self.height() // 2))), 0
                p2 = int(self.ag_x_to_plot_x(obj.x(-self.height() // 2))), self.height()
                self.painter.drawLine(*p1, *p2)
            except ValueError:
                y = int(self.ag_y_to_plot_y(obj.y(0)))
                self.painter.drawLine(0, y, self.width(), y)
        elif isinstance(obj, ag.Triangle):
            self.draw(obj.s1, color)
            self.draw(obj.s2, color)
            self.draw(obj.s3, color)

        self.painter.setBrush(brush)

    def ag_x_to_plot_x(self, x):
        return self.width() // 2 + x

    def ag_y_to_plot_y(self, y):
        return self.height() // 2 - y

    def plot_x_to_ag_x(self, x):
        return x - self.width() // 2

    def plot_y_to_ag_y(self, y):
        return self.height() // 2 - y

    def set_pen(self, color, thickness, line_type=1):
        self.painter.setPen(QPen(color, int(thickness), line_type))
