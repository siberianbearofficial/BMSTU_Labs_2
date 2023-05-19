class Line:
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def rotate(self, point, angle):
        self.p1.rotate(point, angle)
        self.p2.rotate(point, angle)
