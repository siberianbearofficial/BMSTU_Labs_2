def fib_to_10(source):
    x = map(int, reversed(source))
    fib = fibonacci()
    ready = 0
    for el in x:
        ready += el * next(fib)
    del fib
    return ready


def fibonacci():
    prev = curr = 1
    yield 1
    while True:
        prev, curr = curr, prev + curr
        yield curr


if __name__ == '__main__':
    print('Test:')
    a = '1001'
    print(fib_to_10(a))
