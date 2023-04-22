def encode_char(c, p, status):
    for i in range(status * 3, (status + 1) * 3):
        yield ((p[i % 3] & 254) | ((c >> (7 - i)) & 1)) if i < 8 else p[i % 3]


def decode_pixel(p):
    for i in range(3):
        yield p[i] & 1


def decode_str(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError('Не удалось расшифровать это изображение')


def decode(pxs, size):
    s = bytearray([0])
    k = 0
    for i in range(size[0]):
        for j in range(size[1]):
            for p in decode_pixel(pxs[i, j]):
                if k % 9 < 8:
                    s[-1] = s[-1] << 1 | p
                elif not s[-1]:
                    s.pop()
                    return decode_str(s)
                else:
                    s.append(0)
                k += 1
    return decode_str(s)


def encode(pxs, size, s):
    if len(s) + 1 >= (size[0] * size[1]) // 3:
        raise ValueError('Слишком длинная строка. '
                         'Используйте другую или выберите изображение с более высоким разрешением.')
    k = 0
    s = (s + '\0').encode('utf-8')
    for i in range(size[0]):
        for j in range(size[1]):
            if k // 3 >= len(s):
                break
            pxs[i, j] = tuple(encode_char(s[k // 3], pxs[i, j], k % 3))
            k += 1


if __name__ == '__main__':
    from PIL import Image
    img = Image.open('/home/aleksei/Desktop/test_img.bmp')
    pxs_ = img.load()
    s_ = ((26 * 30) // 3 - 3) // 2 * 'ab' + '\0'
    encode(pxs_, img.size, s_)
    print(decode(pxs_, img.size))
