class Polygon:
    def __init__(self, points, bg_color, border_color=None):
        self.points = points
        self.bg_color = bg_color
        self.border_color = border_color

    def __str__(self):
        return f'Polygon({self.points}, self.bg_color, self.border_color)'

    def move(self, dx, dy):
        for p in self.points:
            p.move(dx, dy)

    def rotate(self, point, angle):
        for p in self.points:
            p.rotate(point, angle)
