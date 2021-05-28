#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from coloring import boost_color
from compare import list_mean_rgb,compare1,screening

if __name__ == '__main__':
    im = Image.open('./doom+game/1.jpg')
    images, l = list_mean_rgb()
    pix = (8,8)
    # print(im.size, '\n')
    indices = pixels_by_size(im, pix)
    # print('number of grid by size 64x64', len(indices))
    print(len(indices))
    for index in indices:
        # print(index)
        grid = im.crop(index)
        grid_rgb = mean_img_rgb(grid)
        # piece1 = images[screening(grid_rgb,l)[1]]
        piece1 = images[compare1(grid_rgb, l)[1]]
        # piece = Image.new('RGB', (64, 64), grid_rgb)
        piece = Image.open('./pic/'+piece1)
        piece_resize = piece.resize(pix)
        piece_boost = boost_color(piece_resize, grid_rgb)
        #im.paste(piece_resize, index[:2])
        im.paste(piece_boost, index[:2])
        # print(grid_rgb)
        # print()
    im.show()
    im.close()



