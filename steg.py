from PIL import Image
import numpy as np
import random
import sys

# @Author: Kai Ding
# @Param: information and image carrier(PNG or BMP)
# This program is going implemented the Steganography and return the new image with information
start = "111111110"
stop = "000000001"

def str2binary(value):
    result = ''
    for ele in value.encode():
        result += '{0:08b}'.format(ele)
    # generate random bits to sucre the information
    random_bits = '{0:08b}'.format(random.randint(29, 312))
    result = random_bits + start + result + stop
    return result


# implement least significant bit solution, which replaced each pixel's RGBa lsb to the information
def lsb(info, image_name):
    # generate the hide text binary form and insert into start and stop signal.
    hide_text = str2binary(info)
    im = Image.open(image_name)
    # convert the image to pixels matrix
    pixels = np.asarray(im).copy()
    # The max size of the information will be each pixel * 4 (RGBa)
    if len(hide_text) > len(pixels) * len(pixels[0]) * len(pixels[0][0]):
        print(
            "The size of information is too large for the carrier, "
            "please short your information or change a larger size image.")
        sys.exit()
    index = 0

    for row in pixels:
        for col in row:
            for element in range(len(col)):
                if index < len(hide_text):
                    bi_rgb = '{0:08b}'.format(col[element])
                    bi_rgb = bi_rgb[:-1] + hide_text[index]
                    col[element] = int(bi_rgb, 2)
                index += 1
    array = np.array(pixels, dtype=np.uint8)
    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new_' + image_name)


if __name__ == '__main__':
    info = sys.argv[1]
    image_name = sys.argv[2]
lsb(info, image_name)
