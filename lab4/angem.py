class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


class Vector:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


class Line:
    def __init__(self, p: Point, v: Vector):
        self.p = p
        self.v = v
