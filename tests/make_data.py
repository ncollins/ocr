import Image
from random import random

im = Image.new("L",(100,100))

for i in range(100):
    for j in range(100):
        im.putpixel((i,j),int(random()*256))

im.save("test_image.png")
