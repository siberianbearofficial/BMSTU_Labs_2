from lab5.figures.anim_object import AnimObject
from lab5.figures.polygon import Polygon
from lab5.figures.circle import Circle
from lab5.figures.point import Point


class Asteroid3(AnimObject):
    def __init__(self, x, y):
        self.bg_color = '#9B8F6F'
        self.border_color = '#4E4630'

        self.border = Polygon(
            [Point(13, 91), Point(7, 113), Point(13, 142), Point(2, 157), Point(2, 179), Point(18, 204), Point(36, 217),
             Point(38, 238), Point(68, 256), Point(81, 268), Point(98, 282), Point(118, 278), Point(134, 282),
             Point(144, 278), Point(190, 282), Point(208, 274), Point(236, 268), Point(261, 268), Point(280, 259),
             Point(299, 252), Point(314, 235), Point(328, 206), Point(340, 188), Point(338, 157), Point(344, 133),
             Point(338, 117), Point(338, 108), Point(334, 91), Point(314, 59), Point(296, 48), Point(286, 41),
             Point(280, 33), Point(240, 20), Point(224, 7), Point(197, 2), Point(166, 2), Point(146, 7), Point(124, 4),
             Point(81, 22), Point(60, 41), Point(41, 52), Point(32, 69), Point(13, 91)], self.bg_color,
            self.border_color)

        self.craters = [
            Circle(Point(127, 106), 50, self.border_color),
            Circle(Point(210, 188), 28, self.border_color),
            Circle(Point(127, 227), 21, self.border_color),
            Circle(Point(70, 160), 14, self.border_color),
            Circle(Point(238, 74), 24, self.border_color),
            Circle(Point(191, 59), 14, self.border_color),
            Circle(Point(54, 101), 9, self.border_color),
            Circle(Point(302, 156), 16, self.border_color),
            Circle(Point(242, 130), 10, self.border_color),
            Circle(Point(294, 110), 12, self.border_color),
            Circle(Point(48, 200), 12, self.border_color),
            Circle(Point(20, 170), 6, self.border_color),
            Circle(Point(24, 120), 6, self.border_color),
            Circle(Point(128, 20), 10, self.border_color),
            Circle(Point(290, 206), 22, self.border_color),
            Circle(Point(216, 255), 7, self.border_color),
        ]

        super().__init__(Point(x, y))
