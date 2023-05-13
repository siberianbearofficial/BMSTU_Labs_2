class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise NotImplementedError

    def __str__(self):
        return f'Point({self.x:4g}, {self.y:4g})'

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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise NotImplementedError

    def norm(self):
        return self / abs(self)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def v_mul(v1, v2):
        return v1.x * v2.y - v1.y * v2.x


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.v1 = Vector(self.p2, self.p3)
        self.v2 = Vector(self.p1, self.p3)
        self.v3 = Vector(self.p2, self.p1)

    def __eq__(self, other):
        return (self.p1 == other.p1) and (self.p2 == other.p2) and (self.p3 == other.p3)

    def __str__(self):
        return f'Triangle({self.p1}, {self.p2}, {self.p3})'

    def __repr__(self):
        return self.__str__()

    def area(self):
        return abs(Vector.v_mul(self.v1, self.v2)) / 2

    def bisectors(self):
        m1 = self.p2 + self.v1 / (abs(self.v2) / abs(self.v3) + 1)
        m2 = self.p1 + self.v2 / (abs(self.v1) / abs(self.v3) + 1)
        m3 = self.p2 + self.v3 / (abs(self.v2) / abs(self.v1) + 1)
        return Vector(self.p1, m1), Vector(self.p2, m2), Vector(self.p3, m3)
