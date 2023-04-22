def invert_pixel(p):
    for k in range(3):
        yield 255 - p[k]


def invert(pxs, size):
    for i in range(size[0]):
        for j in range(size[1]):
            pxs[i, j] = tuple(invert_pixel(pxs[i, j]))


if __name__ == '__main__':
    from PIL import Image
    img = Image.open('/home/aleksei/Desktop/image.bmp')
    pxs_ = img.load()
    invert(pxs_, img.size)
    img.show()
