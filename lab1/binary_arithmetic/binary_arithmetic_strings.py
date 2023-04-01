"""
Module for binary arithmetic with strings as numbers
"""


import lab1.binary_arithmetic.signed_binary_arithmetic as sba


def bin_sum(a: str, b: str):
    """
    Function that adds two signed binary numbers given as strings
    :param a: first term
    :param b: second term
    :return: sum
    """
    sba_a = from_string(a)
    sba_b = from_string(b)
    sba_sum = sba.bin_sum(sba_a, sba_b)
    res = to_string(sba_sum)
    return res


def bin_sub(a: str, b: str):
    """
    Function that subtracts from one signed binary number given as string another
    :param a: reduced
    :param b: subtracted
    :return: difference
    """
    sba_a = from_string(a)
    sba_b = from_string(b)
    sba_sub = sba.bin_sub(sba_a, sba_b)
    res = to_string(sba_sub)
    return res


def bin_mul(a: str, b: str):
    """
    Function that multiplies two signed binary numbers given as strings
    :param a: first multiplier
    :param b: second multiplier
    :return: product
    """
    sba_a = from_string(a)
    sba_b = from_string(b)
    sba_mul = sba.bin_mul(sba_a, sba_b)
    res = to_string(sba_mul)
    return res


def from_string(source: str):
    """
    Function that converts given string into signed binary number
    :param source: string for conversion
    :return: signed binary number
    :raise AttributeError: if not a valid number is given as a string argument
    """
    ready = list()
    is_positive = source[0] != '-'
    for el in reversed(source):
        if el in '01':
            ready.append(int(el))
        elif el in '.,':
            ready.append('.')
        elif el != '-':
            print(f'Не удалось обработать: {source}')    # TODO: remove print after fixing exception's bug
            raise AttributeError(f'Не удалось обработать: {source}')
    return is_positive, ready


def to_string(c):
    """
    Function that converts given signed binary number into string
    :param c: signed binary number
    :return: ready string
    """
    if c[1] == [0]:
        return '0'
    return f'{"-" if not c[0] else ""}{"".join(map(str, reversed(c[1])))}'


if __name__ == '__main__':
    # Basic test (integers)

    num1 = '-10.1'
    num2 = '-100.01'

    print('Basic test (integers):')
    print('Num1', num1)
    print('Num2', num2)
    print('Sum:', bin_sum(num1, num2))
    print('Sub:', bin_sub(num1, num2))
    print('Mul:', bin_mul(num1, num2))
