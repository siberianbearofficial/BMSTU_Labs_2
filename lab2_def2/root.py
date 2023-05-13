def root(func, a, b, eps):
    interval = a, b

    middle = (a + b) / 2
    while abs(func(middle)) >= eps and abs(a - b) > eps:
        if func(a) * func(middle) > 0:
            a = middle
        else:
            b = middle
        middle = (a + b) / 2

    if interval[0] <= middle <= interval[1]:
        return 0, middle
    else:
        return 1,


if __name__ == '__main__':
    from math import sin
    print(*root(sin, -8, -4, 0.001))
