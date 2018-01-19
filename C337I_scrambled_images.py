from PIL import Image


def unscramble(filename):
    img = Image.open(filename)
    width, height = img.size
    hsv = img.convert('HSV')
    data = list(hsv.getdata())
    new_data = []
    for row in range(height):
        row_data = data[row * width:(row + 1) * width]
        shift = min(i for i, pixel in enumerate(row_data) if pixel[1])
        new_data.extend(row_data[shift:width] + row_data[:shift])
    hsv.putdata(new_data)
    return hsv


if __name__ == '__main__':
    for image in (1, 2, 3):
        unscramble(f'input/scrambled_images_input{image}.png').show()
