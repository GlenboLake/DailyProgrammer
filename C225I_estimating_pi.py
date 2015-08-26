# Broken in Python 3
from PIL import Image
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def get_pixel_data(image):
    data = image.tobytes()

    def chunk(data, size):
        for i in range(0, len(data), size):
            yield data[i:i + size]
    pixels = [tuple([ord(x) for x in y]) for y in chunk(data, 3)]
    return list(chunk(pixels, image.size[0]))


def approximate(imname):
    im = Image.open(imname)
    data = get_pixel_data(im)
    diameter = 0
    area = 0
    for row in data:
        count = row.count(BLACK)
        area += count
        if count > diameter:
            diameter = count
    return float(area) / ((diameter / 2)**2)

#print approximate('input/pi1.png')
#print approximate('input/pi2.png')

#-------------------#
# Try using C and A #
#-------------------#


def adjacent(nearby, image, x, y, check):
    for dx, dy in nearby:
        try:
            if image.getpixel((x + dx, y + dy)) == check:
                return True
        except IndexError:
            pass
    return False


def adjacent_4(image, x, y, check):
    return adjacent([(0, 1), (1, 0), (0, -1), (-1, 0)],
                    image, x, y, check)


def adjacent_8(image, x, y, check):
    return adjacent([(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
                    image, x, y, check)


def adv_approximage(imname):
    im = Image.open(imname)
    w, h = im.size
    area = 0
    big_circum = 0
    small_circum = 0
    for x in range(w):
        for y in range(h):
            if im.getpixel((x, y)) == BLACK:
                area += 1
                if adjacent_4(im, x, y, WHITE):
                    small_circum += 1
                if adjacent_8(im, x, y, WHITE):
                    big_circum += 1
    C = (big_circum+small_circum)/2.0
    print('poor approximation:', C**2/(4*area))
    return area

area = adv_approximage('input/pi1.png')
print('better approximation:', float(area) / (500**2))
