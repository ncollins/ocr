# Python OCR

import sys
import Image
import itertools
import numpy as np

if sys.version_info.major < 3:
    range = xrange 

# functions

def image_to_array(im, reshape=True):
    """
    Converts a PIL Image object into a numpy array representing
    a greyscale image.
    Parameters:
        im - a PIL Image object
        reshape (default: True) - if True then returns a 2D image
                                otherwise it returns a flat 1D araray.
    Output:
        A numpy array.
    """
    im_greyscale = im.convert("L")
    width, height = im_greyscale.size
    im_array = np.ndarray(width * height)
    for i, p in enumerate(im_greyscale.getdata()):
        im_array[i] = p
    if reshape:
        im_array.shape = (height, width)
    return im_array


def array_to_image(array):
    height, width = array.shape
    im = Image.new('L', (width, height), 255)
    for x in range(width):
        for y in range(height):
            im.putpixel((x,y), array[y][x])
    return im


def windows0(im, rectangles, output_size):
    im_width, im_height = im.size
    for dx, dy in rectangles:
        for x0, y0 in itertools.product(range(im_width-dx+1),range(im_height-dy+1)):
            yield im.crop((x0, y0, x0+dx, y0+dy))


def windows(im, rectangles, output_size):
    """
    Parameters:
    im - a PIL image
    rectangles - a list of (width, height) pairs of rectangle sizes
    output_size - the desired output size in (width, height) format
    """
    im_width, im_height = im.size
    for dx, dy in rectangles:
        for x0, y0 in itertools.product(range(im_width-dx+1),range(im_height-dy+1)):
            yield im.transform(output_size, Image.EXTENT, (x0, y0, x0+dx, y0+dy))


def array_windows(im, rectangles, output_size):
    """
    Parameters:
    im - a PIL image
    rectangles - a list of (width, height) pairs of rectangle sizes
    output_size - the desired output size in (width, height) format
    """
    return (image_to_array(w) for w in windows(im, rectangles, output_size))


if __name__ == '__main__':
    # testing code
    testfile = "data/hk.png"
    im_raw = Image.open(testfile)
    im_array = image_to_array(im_raw)
