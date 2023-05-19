from lab5.figures.point import Point
from lab5.figures.circle import Circle
from lab5.figures.polygon import Polygon
from lab5.figures.line import Line


class AnimObject:
    def __init__(self, pos):
        self.pos = pos

        self.speed = (0, 0)
        self.acceleration = (0, 0)

        self.rotation_point = self.center()
        self.rotation_angle = None
        self.move(pos.x, pos.y)

    def center(self):
        min_point, max_point = None, None
        for obj in self.objects():
            if isinstance(obj, Circle):
                min_point = Point.min_point(min_point, obj.center) if min_point else obj.center
                max_point = Point.max_point(max_point, obj.center) if max_point else obj.center
            elif isinstance(obj, Polygon):
                for point in obj.points:
                    min_point = Point.min_point(min_point, point) if min_point else point
                    max_point = Point.max_point(max_point, point) if max_point else point
        return Point.mid_point(min_point, max_point) if min_point and max_point else None

    def set_speed(self, vx, vy):
        self.speed = vx, vy
        return self

    def set_rotation_angle(self, angle):
        self.rotation_angle = angle
        return self

    def move(self, dx, dy):
        for obj in self.objects():
            obj.move(dx, dy)
        self.rotation_point.move(dx, dy)

    def update_pos(self):
        self.move(*self.speed)
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])

    def rotate(self, alpha=None):
        if alpha is not None:
            for obj in self.objects():
                obj.rotate(self.rotation_point, alpha)
        elif self.rotation_angle is not None:
            self.rotate(self.rotation_angle)

    def objects(self):
        for field in self.__dict__:
            if isinstance(self.__dict__[field], (Circle, Polygon, Line)):
                yield self.__dict__[field]
            elif isinstance(self.__dict__[field], (list, tuple)):
                for i in range(len(self.__dict__[field])):
                    if isinstance(self.__dict__[field][i], (Circle, Polygon, Line)):
                        yield self.__dict__[field][i]
