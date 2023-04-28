"""
Заданы два множества точек. Найти такой
треугольник с вершинами – точками первого
множества, внутри которого находится одинаковое
количество точек из первого и из второго множеств.
"""

from angem import Triangle


def find_triangle(ps1, ps2):
    for i1 in range(len(ps1) - 2):
        for i2 in range(i1 + 1, len(ps1) - 1):
            for i3 in range(i2 + 1, len(ps1)):
                triangle = Triangle(ps1[i1], ps1[i2], ps1[i3])
                if check_triangle(triangle, ps1, ps2):
                    yield triangle


def check_triangle(triangle, ps1, ps2):
    c1 = sum(triangle.inside(p) for p in ps1)
    c2 = sum(triangle.inside(p) for p in ps2)
    return c1 == c2
