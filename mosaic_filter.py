#!/usr/bin/python
from sizing import dimention
from PIL import Image

im = Image.open('./pic/test.png')
print(dimention(im))
im.close()
