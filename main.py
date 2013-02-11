# Python OCR

testfile = "data/hk.png"

import ImageFile

fp = open(testfile, "rb")

p = ImageFile.Parser()

while 1:
    s = fp.read(1024)
    if not s:
        break
    p.feed(s)

im = p.close()

#im.save("copy.jpg")
