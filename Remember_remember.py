from PIL import Image
import numpy


def decipher_terrorist_code(path: str) -> str:
    """
    The function deciphers a code by black pixels in an image.
    The code is encrypted in the image by order from left to right by columns.
    :param path: Name/Path of the image file.
    :return: String of the decipher code.
    """
    blacks = numpy.where(numpy.array(Image.open(path)) == 1)
    black_pixels = sorted(list(zip(blacks[0], blacks[1])), key=lambda element: element[1])
    return "".join(chr(element[0]) for element in black_pixels)


def main():
    print(decipher_terrorist_code("code.png"))


if __name__ == '__main__':
    main()
