# Python OCR

import sys
import Image
import itertools
import numpy as np

if sys.version_info.major < 3:
    range = xrange 

# test data

testfile = "data/hk.png"

# code

im_raw = Image.open(testfile)

def image_to_array(im):
    """
    Converts a PIL Image object into a numpy array representing
    a greyscale image.
    """
    im_greyscale = im_raw.convert("L")
    width, height = im_greyscale.size
    im_array = np.ndarray(width * height)
    for i, p in enumerate(im_greyscale.getdata()):
        im_array[i] = p
    im_array.shape = (width,height)
    return im_array

im_array = image_to_array(im_raw)

# sliding windows

def windows(im_array, rectangles):
    """
    Parameters:
    im_array - a numpy array representing a greyscale image
    rectangles - a list of (width, height) pairs of rectangle sizes
    """
    width, height = im_array.shape
    for dx, dy in rectangles:
        for x0, y0 in itertools.product(range(width-dx),range(height-dy)): 
            yield im_array[x0:x0+dx, y0:y0+dy]
