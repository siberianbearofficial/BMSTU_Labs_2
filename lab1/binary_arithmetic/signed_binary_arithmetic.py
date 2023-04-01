"""
Module for signed binary arithmetic
"""


import lab1.binary_arithmetic.unsigned_binary_arithmetic as us


def gt(a, b):
    """
    Function returns True if first signed binary num is greater than second
    :param a: first num
    :param b: second num
    :return: result of comparison
    """

    if a[0] and b[0]:
        res = us.gt(a[1], b[1])
    elif a[0]:
        res = True
    elif b[0]:
        res = False
    else:
        res = not us.gt(a[1], b[1])

    return res


def bin_sum(x, y):
    """
    Function that adds two signed binary numbers
    :param x: first term
    :param y: second term
    :return: sum
    """
    if x[0] and y[0]:
        return True, us.bin_sum(x[1], y[1])
    elif x[0]:
        return bin_sub(x, (True, y[1]))
    elif y[0]:
        return bin_sub((True, x[1]), y)
    else:
        return False, us.bin_sum(x[1], y[1])


def bin_sub(x, y):
    """
    Function that subtracts from one signed binary number another
    :param x: reduced
    :param y: subtracted
    :return: difference
    """
    if x[0] and y[0]:
        if gt(x, y):
            return True, us.bin_sub(x[1], y[1])
        else:
            return False, us.bin_sub(y[1], x[1])
    elif x[0]:
        return True, us.bin_sum(x[1], y[1])
    elif y[0]:
        return False, us.bin_sum(x[1], y[1])
    else:
        if gt(x, y):
            return True, us.bin_sub(y[1], x[1])
        else:
            return False, us.bin_sub(x[1], y[1])


def bin_mul(x, y):
    """
    Function that multiplies two signed binary numbers
    :param x: first multiplier
    :param y: second multiplier
    :return: product
    """
    if x[0] and y[0] or not x[0] and not y[0]:
        return True, us.bin_mul(x[1], y[1])
    else:
        return False, us.bin_mul(x[1], y[1])
