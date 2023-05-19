from math import sin, cos


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, point, angle):
        dx = self.x - point.x
        dy = self.y - point.y
        self.x = dx * cos(angle) - dy * sin(angle) + point.x
        self.y = dx * sin(angle) + dy * cos(angle) + point.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def min_point(p1, p2):
        return Point(min(p1.x, p2.x), min(p1.y, p2.y))

    @staticmethod
    def max_point(p1, p2):
        return Point(max(p1.x, p2.x), max(p1.y, p2.y))

    @staticmethod
    def mid_point(p1, p2):
        return Point((p1.x + p2.x) // 2, (p1.y + p2.y) // 2)
