from skimage.transform import hough, probabilistic_hough
from skimage.filter import canny, sobel
#from skimage import data

import numpy as np
#import matplotlib.pyplot as plt

# Line finding, using the Probabilistic Hough Transform

import Image
import ImageDraw
from sliding_windows import image_to_array, array_to_image

im = Image.open('data/hk_eng_crop.png')
im_array = image_to_array(im)
im_arary = im_array / 255

#theta = np.ones(1) * np.pi / 2
r = range(-50,50)
r_theta = [np.pi/2 + x*0.001 for x in r]
theta = np.array(r_theta)

edges = canny(im_array, 2, 1, 25)

lines = probabilistic_hough(edges, threshold=5, line_length=20,
                            line_gap=20, theta=theta)


# find clusters of lines

def draw_lines(lines, shape):
    """
    Find clusters of lines.
    """
    im = Image.new('L', shape, 255)
    draw = ImageDraw.Draw(im)
    for (x0, y0), (x1, y1) in lines:
        draw.line([(x0, y0), (x1, y1)], width = 1)
    return im

im_lines = draw_lines(lines, im.size)
