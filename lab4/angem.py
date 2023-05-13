class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise NotImplementedError

    def __str__(self):
        return f'Point({self.x:4g}, {self.y:4g})'

    def __repr__(self):
        return self.__str__()


class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Segment({self.p1}, {self.p2})'

    def __repr__(self):
        return self.__str__()


class Vector:
    def __init__(self, p1: Point | int | float, p2: Point | int | float):
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.p1 = p1
            self.p2 = p2
            self.x = self.p2.x - self.p1.x
            self.y = self.p2.y - self.p1.y
        else:
            self.p1, self.p2 = None, None
            self.x = p1
            self.y = p2

    def __abs__(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __truediv__(self, other: int | float):
        return Vector(self.x / other, self.y / other)

    def norm(self):
        return self / abs(self)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()


class Line:
    def __init__(self, p: Point, obj2: Vector | Point):
        self.p = p
        if isinstance(obj2, Vector):
            self.v = obj2
        else:
            self.v = Vector(p, obj2)

    def x(self, y):
        if self.v.y != 0:
            return (y - self.p.y) / self.v.y * self.v.x + self.p.x
        raise ValueError('Horizontal line')

    def y(self, x):
        if self.v.x != 0:
            return (x - self.p.x) / self.v.x * self.v.y + self.p.y
        raise ValueError('Vertical line')

    def __str__(self):
        return f'Line((x - {self.p.x})/{self.v.x} = (y - {self.p.y})/{self.v.y})'

    def __repr__(self):
        return self.__str__()


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.s1 = Segment(p2, p3)
        self.s2 = Segment(p1, p3)
        self.s3 = Segment(p1, p2)

    def __str__(self):
        return f'Triangle({self.p1}, {self.p2}, {self.p3})'

    def __repr__(self):
        return self.__str__()

    def inside(self, p: Point):
        if not isinstance(p, Point):
            raise NotImplementedError

        d1 = Triangle.__sign(p, self.p1, self.p2)
        d2 = Triangle.__sign(p, self.p2, self.p3)
        d3 = Triangle.__sign(p, self.p3, self.p1)

        has_neg = (d1 <= 0) or (d2 <= 0) or (d3 <= 0)
        has_pos = (d1 >= 0) or (d2 >= 0) or (d3 >= 0)

        return not (has_neg and has_pos)

    @staticmethod
    def __sign(p1, p2, p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)
