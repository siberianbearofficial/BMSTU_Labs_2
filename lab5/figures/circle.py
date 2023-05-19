class Circle:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def rotate(self, point, angle):
        self.center.rotate(point, angle)

    def __str__(self):
        return f'Circle({self.center}, {self.radius}, self.border_color)'
