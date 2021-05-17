#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb

im = Image.open('./pic/test.png')
indices = pixels_by_size(im, (64, 64))
print('number of grid by size 64x64', len(indices))

for index in indices:
    grid = im.crop(index)
    grid_rgb =  mean_img_rgb(grid)
    print(grid_rgb, grid.size)
    piece = Image.new('RGB', (64, 64), grid_rgb)
    im.paste(piece, index[:2])
    
im.show()
im.close()



