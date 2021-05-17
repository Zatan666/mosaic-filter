#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb

im = Image.open('./pic/test.png')
indices = pixels_by_size(im, (64, 64))
print('number of grid by size 64x64', len(indices))

for index in indices:
    
    grid_rgb =  mean_img_rgb(im.crop(index))
    piece = Image.new('RGB', (63, 63), grid_rgb)
    im.paste(piece, index)
    
im.show()
im.close()



