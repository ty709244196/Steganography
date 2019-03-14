from PIL import Image
import numpy as np
import sys

start = "111111110"
stop = "000000001"


# @Author: Kai Ding
# @Param: image name
# This program is going to decode the Steganography and return the plain text to the terminal

# This function will decode the image and return the information in binary
def decode(image_name):
    im = Image.open(image_name)
    # Convert image to pixels matrix
    pixels = np.asarray(im)
    result_list = []
    return_result = []
    flag = False
    for row in pixels:
        for col in row:
            for element in col:
                ele = '{0:08b}'.format(element)[-1]
                result_list.append(ele)
                if flag:
                    return_result.append(ele)
                    if contain(return_result, stop):
                        return return_result
                if not flag and contain(result_list, start):
                    flag = True


# This function implanted slide window algorithm to check the start/stop signal is in the result
def contain(result_list, pattern):
    if len(result_list) < len(pattern):
        return False
    for i in range(len(result_list) - len(pattern) + 1):
        if result_list[i:i + len(pattern)] == list(pattern):
            return True
    return False


if __name__ == '__main__':
    image_name = sys.argv[1]
    return_list = decode(image_name)[:-len(stop)]
    bi_information = ''.join(return_list)
    p_information = ''
    # convert it back to utf-8 encode character
    for i in range(len(bi_information) // 8):
        p_information += (chr(int(bi_information[i * 8:i * 8 + 8], 2)))

print(p_information)
