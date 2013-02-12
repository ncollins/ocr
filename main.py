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


# sliding windows

def windows0(im, rectangles, output_size):
    im_width, im_height = im.size
    for dxp1, dyp1 in rectangles:
        dx, dy = dxp1-1, dxp1-1
        for x0, y0 in itertools.product(range(im_width-dx),range(im_height-dy)): 
            yield im.crop((x0, y0, x0+dx, y0+dy))

def windows(im, rectangles, output_size):
    """
    Parameters:
    im - a PIL image
    rectangles - a list of (width, height) pairs of rectangle sizes
    output_size - the desired output size in (width, height) format
    """
    im_width, im_height = im.size
    for dxp1, dyp1 in rectangles:
        dx, dy = dxp1-1, dxp1-1
        for x0, y0 in itertools.product(range(im_width-dx),range(im_height-dy)): 
            #if x0 < 3:
                #print (x0,y0,x0+dx,y0+dy)
            yield im.transform(output_size, Image.EXTENT, (x0, y0, x0+dx, y0+dy))


def array_windows(im, rectangles, output_size):
    """
    Parameters:
    im - a PIL image
    rectangles - a list of (width, height) pairs of rectangle sizes
    output_size - the desired output size in (width, height) format
    """
    return (image_to_array(w) for w in windows(im, rectangles, output_size))


# testing code

im_raw = Image.open(testfile)
im_array = image_to_array(im_raw)
