from lab5.figures.anim_object import AnimObject
from lab5.figures.polygon import Polygon
from lab5.figures.circle import Circle
from lab5.figures.point import Point


class Asteroid1(AnimObject):
    def __init__(self, x, y):
        self.bg_color = '#9B8F6F'
        self.border_color = '#4E4630'

        self.border = Polygon([
            Point(13, 57),
            Point(5, 70),
            Point(2, 81),
            Point(5, 95),
            Point(24, 114),
            Point(53, 129),
            Point(83, 132),
            Point(113, 122),
            Point(124, 107),
            Point(145, 105),
            Point(163, 95),
            Point(163, 88),
            Point(175, 60),
            Point(164, 46),
            Point(164, 32),
            Point(153, 17),
            Point(128, 5),
            Point(85, 5),
            Point(53, 3),
            Point(26, 19),
            Point(26, 42),
            Point(13, 57),
        ], self.bg_color, self.border_color)

        self.craters = [
            Circle(Point(57, 23), 16, self.border_color),
            Circle(Point(50, 69), 12, self.border_color),
            Circle(Point(97, 51), 30, self.border_color),
            Circle(Point(145, 75), 15, self.border_color),
            Circle(Point(33, 97), 8, self.border_color),
            Circle(Point(79, 106), 17, self.border_color),
            Circle(Point(49, 115), 6, self.border_color),
        ]

        super().__init__(Point(x, y))
