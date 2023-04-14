def root(func, a, b, eps):
    code = 0
    interval = a, b
    while True:
        sec = secant(func, a, b)
        if sec is None:
            code = 1
            break
        a, b = b, b - sec
        if abs(sec) < eps:
            break
    if interval[0] <= (a + b) / 2 <= interval[1]:
        return code, a
    else:
        return 1,


def secant(func, x0, x1):
    f0 = func(x0)
    f1 = func(x1)
    return (f1 * (x1 - x0) / (f1 - f0)) if f0 != f1 else None


if __name__ == '__main__':
    from math import sin
    print(*root(sin, 4, 7, 0.001))
