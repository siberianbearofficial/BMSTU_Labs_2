from lab5.figures.anim_object import AnimObject
from lab5.figures.polygon import Polygon
from lab5.figures.circle import Circle
from lab5.figures.point import Point


class Asteroid2(AnimObject):
    def __init__(self, x, y):
        self.border = Polygon([
            Point(48, 14),
            Point(8, 22),
            Point(2, 29),
            Point(2, 48),
            Point(12, 70),
            Point(25, 86),
            Point(43, 95),
            Point(78, 106),
            Point(162, 106),
            Point(190, 101),
            Point(229, 95),
            Point(250, 80),
            Point(254, 70),
            Point(238, 46),
            Point(224, 22),
            Point(206, 14),
            Point(180, 14),
            Point(150, 7),
            Point(132, 14),
            Point(111, 14),
            Point(74, 2),
            Point(48, 14)
        ], "#9B8F6F", "#4E4630")

        self.craters = [
            Circle(Point(66, 60), 22, "#4E4630"),
            Circle(Point(156, 51), 31, "#4E4630"),
            Circle(Point(76, 20), 10, "#4E4630"),
            Circle(Point(17, 39), 8, "#4E4630"),
            Circle(Point(103, 91), 9, "#4E4630"),
            Circle(Point(210, 82), 10, "#4E4630"),
            Circle(Point(216, 44), 16, "#4E4630"),
        ]

        super().__init__(Point(x, y))
