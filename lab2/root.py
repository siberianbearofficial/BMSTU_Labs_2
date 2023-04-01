import math
from derivative import derivative


def parse_func(f):
    func_error = False
    func = None
    der = None
    der_str = None
    if not f or len(f) >= 5 and f[:6] == 'Error':
        func_error = True
    else:
        try:
            func = eval(f'lambda x: {f}', {'math': math, 'm': math})
            der_str = derivative(f)
            der = eval(f'lambda x: {der_str}', {'math': math, 'm': math})
            der_str = derivative(der_str)
        except:
            func_error = True
    return func_error, func, der, der_str


def root(func, der, a, b, eps, max_iterations):
    code = 0
    count_iterations = 0
    while True:
        sec = secant(func, a, b)
        tan = tangent(func, der, b)
        if tan is None:
            code = 1
            break
        a += sec
        b -= tan
        count_iterations += 1
        if abs(a - b) <= eps or count_iterations > max_iterations:
            break
    return code, (a + b) / 2, count_iterations


def tangent(func, der, x):
    dx = der(x)
    return (func(x) / dx) if dx else None


def secant(func, x0, x1):
    f0 = func(x0)
    f1 = func(x1)
    return (f0 * (x1 - x0) / (f0 - f1)) if f0 != f1 else None


def has_root_in_interval(func, x0, x1):
    try:
        return (func(x0) * func(x1)) <= 0
    except:
        return False


def in_interval(x, a, b):
    return a <= x <= b


def roots(func, step, interval_list, epsilon, max_iterations):
    a, border_b = sorted(interval_list)
    func_error, func, d, _ = parse_func(func)

    if func_error:
        return

    while a < border_b:
        b = min(a + step, border_b)
        if has_root_in_interval(func, a, b):
            code, found_root, count_iterations = root(func, d, a, b, epsilon, max_iterations)
            if code:
                yield 1, count_iterations, '-', '-', [a, b]
            elif max_iterations < count_iterations:
                yield 2, count_iterations, '-', '-', [a, b]
            elif in_interval(found_root, a, b):
                yield 0, count_iterations, func(found_root), found_root, [a, b]
            else:
                yield 3, count_iterations, '-', '-', [a, b]
        a = b
