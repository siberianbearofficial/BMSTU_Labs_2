"""
Дано множество точек. Найти треугольник, для которого разность площадей
треугольников, образованных делением одной из биссектрис, будет минимальна.
"""

from angem import Triangle, Vector


def find_triangle(points):
    min_key, min_key_triangle = None, None
    for i1 in range(len(points) - 2):
        for i2 in range(i1 + 1, len(points) - 1):
            for i3 in range(i2 + 1, len(points)):
                triangle = Triangle(points[i1], points[i2], points[i3])
                key = get_key(triangle)
                if min_key is None or key < min_key:
                    min_key = key
                    min_key_triangle = triangle
    return min_key_triangle


def find_triangle2(points):
    min_key, min_key_triangle = None, None
    for i1 in range(len(points) - 2):
        for i2 in range(i1 + 1, len(points) - 1):
            for i3 in range(i2 + 1, len(points)):
                triangle = Triangle(points[i1], points[i2], points[i3])
                key = get_key2(triangle)
                if min_key is None or key < min_key:
                    min_key = key
                    min_key_triangle = triangle
    return min_key_triangle


def get_key(triangle):
    bis1, bis2, bis3 = triangle.bisectors()
    area1 = abs(abs(Vector.v_mul(bis1, triangle.v2)) / 2 - abs(Vector.v_mul(bis1, triangle.v3)) / 2)
    area2 = abs(abs(Vector.v_mul(bis2, triangle.v1)) / 2 - abs(Vector.v_mul(bis2, triangle.v3)) / 2)
    area3 = abs(abs(Vector.v_mul(bis3, triangle.v1)) / 2 - abs(Vector.v_mul(bis3, triangle.v2)) / 2)
    return min(area1, area2, area3)


def get_key2(triangle):
    v1, v2, v3 = abs(triangle.v1), abs(triangle.v2), abs(triangle.v3)
    area1_k = abs((v2 - v3) / (v2 + v3))
    area2_k = abs((v1 - v3) / (v1 + v3))
    area3_k = abs((v1 - v2) / (v1 + v2))
    return min(area1_k, area2_k, area3_k) * triangle.area()


if __name__ == '__main__':
    from random import randint
    from angem import Point
    from time import time

    for _ in range(100):
        points = [Point(randint(-1000, 1000), randint(-1000, 1000)) for _ in range(100)]

        tt1 = time()
        t1 = find_triangle(points)
        tt1 = time() - tt1
        tt2 = time()
        t2 = find_triangle2(points)
        tt2 = time() - tt2

        if t1 == t2:
            print(tt1, tt2)
        else:
            print('WA', t1, t2)
