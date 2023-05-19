from lab5.figures.anim_object import AnimObject
from lab5.figures.polygon import Polygon
from lab5.figures.point import Point


class Star(AnimObject):
    def __init__(self, x, y):
        self.bg_color = '#FFDFBF'

        self.path = Polygon(
            [Point(20, 4), Point(15, 11), Point(6, 11), Point(14, 16), Point(6, 26), Point(20, 20), Point(30, 26),
             Point(26, 18), Point(32, 11), Point(24, 11), Point(20, 4)], self.bg_color)

        super().__init__(Point(x, y))
