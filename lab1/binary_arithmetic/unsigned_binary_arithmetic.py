"""
Module for unsigned binary arithmetic
"""


def gt(a, b):
    """
    Function returns True if first unsigned binary num is greater than second
    :param a: first num
    :param b: second num
    :return: result of comparison
    """

    add_zeros(a, b)

    if len(a) == len(b):
        for i in range(len(a) - 1, -1, -1):
            if a[i] != b[i]:
                res = a[i]
                break
        else:
            res = False
    else:
        res = len(a) > len(b)

    remove_zeros(a)
    remove_zeros(b)

    return res


def bin_sum(a, b):
    """
    Function that adds two unsigned binary numbers
    :param a: first term
    :param b: second term
    :return: sum
    """
    add_zeros(a, b)
    overflow = 0
    res = list()
    for i in range(len(a)):
        if a[i] == '.':
            res.append('.')
        else:
            sum_ = a[i] + b[i] + overflow
            overflow = sum_ // 2
            res.append(sum_ % 2)
    res.append(overflow)
    remove_zeros(res)
    return res


def bin_sub(a, b):
    """
    Function that subtracts from one unsigned binary number another
    :param a: reduced
    :param b: subtracted
    :return: difference
    """
    add_zeros(a, b)
    overflow = 0
    res = list()
    for i in range(len(a)):
        if a[i] == '.':
            res.append('.')
        else:
            sub_ = a[i] - overflow - b[i]
            overflow = sub_ < 0
            res.append(abs(sub_) % 2)
    remove_zeros(res)
    return res


def calculate_point_index(list1, list2):
    point_pos = 0
    if '.' in list1:
        point_pos += list1.index('.')
    if '.' in list2:
        point_pos += list2.index('.')
    return point_pos


def move_point(list_with_point_as_element, point_new_pos):
    if '.' in list_with_point_as_element:
        list_with_point_as_element.remove('.')
    list_with_point_as_element.insert(point_new_pos, '.')


def remove_point(*args):
    for arg in args:
        if '.' in arg:
            arg.remove('.')


def bin_mul(a, b):
    """
    Function that multiplies two unsigned binary numbers
    :param a: first multiplier
    :param b: second multiplier
    :return: product
    """

    remove_zeros(a)
    remove_zeros(b)
    point_index = calculate_point_index(a, b)
    remove_point(a, b)

    c = list()
    for el in b:
        if el:
            c = bin_sum(c, a)
        a.insert(0, 0)
    move_point(c, point_index)
    remove_zeros(c)
    return c


def add_zeros(a, b):
    """
    Function that adds insignificant zeros to both nums to align them in length
    :param a: first num
    :param b: second num
    :return:
    """
    if '.' not in a and '.' not in b:
        add_zeros_to_ints(a, b)
        return

    if '.' not in a:
        to_float_signed_bin_num(a)
    elif '.' not in b:
        to_float_signed_bin_num(b)

    point_index_a = a.index('.')
    point_index_b = b.index('.')

    len_after_point_a = len(a) - point_index_a - 1
    len_after_point_b = len(b) - point_index_b - 1

    while point_index_a < point_index_b:
        a.insert(0, 0)
        point_index_a += 1
    while point_index_b < point_index_a:
        b.insert(0, 0)
        point_index_b += 1

    while len_after_point_a < len_after_point_b:
        a.append(0)
        len_after_point_a += 1
    while len_after_point_b < len_after_point_a:
        b.append(0)
        len_after_point_b += 1


def add_zeros_to_ints(a, b):
    """
    Function that adds insignificant zeros to both integer nums to align them in length
    :param a: first num
    :param b: second num
    :return:
    """
    while len(a) < len(b):
        a.append(0)
    while len(b) < len(a):
        b.append(0)


def to_float_signed_bin_num(c):
    """
    Function that converts integer signed binary number into a float one
    :param c: integer signed binary number
    :return:
    """
    c.insert(0, '.')
    c.insert(0, 0)


def remove_zeros(c):
    """
    Function that removes insignificant zeros from a signed binary number
    :param c: number
    :return:
    """
    if c == ['.']:
        c.pop()
        c.append(0)

    remove_zeros_before_point(c)
    remove_zeros_after_point(c)


def remove_zeros_before_point(c):
    """
    Function that removes insignificant zeros before point from a signed binary number
    :param c: number
    :return:
    """
    while c != [0]:
        if c[-1] == 1:
            break
        if len(c) > 1:
            if c[-2] == '.':
                break
            c.pop()


def remove_zeros_after_point(c):
    """
    Function that removes insignificant zeros after point from a signed binary number
    :param c: number
    :return:
    """
    if '.' in c:
        while c:
            if c[0] == 1:
                break
            if c[0] == '.':
                c.pop(0)
                break
            c.pop(0)
