# Python OCR

import Image
import numpy as np

# test data

testfile = "data/hk.png"

# code

im_raw = Image.open(testfile)

def image_to_array(im):
    im_greyscale = im_raw.convert("L")
    width, height = im_greyscale.size
    im_array = np.ndarray(width * height)
    for i, p in enumerate(im_greyscale.getdata()):
        im_array[i] = p
    im_array.shape = (width,height)
    return im_array

im_array = image_to_array(im_raw)

# sliding windows

def windows(im_array):
    pass
