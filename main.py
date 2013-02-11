# Python OCR

import Image
import numpy as np

# test data

testfile = "data/hk.png"

# code

im_raw = Image.open(testfile)
im_greyscale = im_raw.convert("L")

width, height = im_greyscale.size

im_array = np.ndarray(width * height)

for p in im_greyscale.getdata():
    im_array[0] = p

im_array.resize((width,height))
