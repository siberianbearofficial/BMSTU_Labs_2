from lab5.figures.point import Point
from lab5.figures.circle import Circle
from lab5.figures.polygon import Polygon
from lab5.figures.anim_object import AnimObject


class SpaceCraft(AnimObject):
    def __init__(self, x, y):
        accent_color = '#EB2626'
        bg_color = '#D6A184'
        window_color = '#A9D9FF'
        flame_color = '#FF842B'
        border_color = '#000000'

        self.main_part = Polygon(
            [Point(90, 346), Point(10, 436), Point(133, 397), Point(133, 430), Point(208, 430), Point(208, 397),
             Point(330, 436), Point(252, 354), Point(170, 28), Point(90, 346)], bg_color, border_color)
        self.flame = Polygon(
            [Point(4, 518), Point(36, 428), Point(133, 388), Point(208, 388), Point(304, 428), Point(363, 498),
             Point(277, 452), Point(301, 518), Point(222, 438), Point(234, 504), Point(192, 452), Point(172, 490),
             Point(152, 452), Point(114, 510), Point(110, 460), Point(46, 542), Point(71, 460), Point(4, 518)],
            flame_color, border_color)
        self.line = Polygon([Point(170, 29), Point(170, 19), Point(170, 29)], border_color)
        self.number = Polygon(
            [Point(170, 298), Point(151, 326), Point(162, 326), Point(170, 312), Point(170, 356), Point(151, 356),
             Point(151, 367), Point(188, 367), Point(188, 356), Point(179, 356), Point(179, 298), Point(170, 298)],
            accent_color, border_color)
        self.window = Circle(Point(170, 242), 34, window_color)
        self.light = Circle(Point(170, 10), 9, accent_color)

        super().__init__(Point(x, y))
