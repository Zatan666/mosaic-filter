#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from coloring import boost_color
from compare import list_mean_rgb,compare1,screening
import time

if __name__ == '__main__':
    tic = time.process_time()
    q = 'forest'
    pix = (16, 16)
    select = 373
    print(f'open {q} {select}.jpg ...')
    im = Image.open(f'pic/{q}/{select}.jpg')
    print('open and cal rgb other pic ...')
    images, l = list_mean_rgb(q, pix, select)
    # print(im.size, '\n')
    indices = pixels_by_size(im, pix)
    # print('number of grid by size 64x64', len(indices))
    comp = len(indices)
    for prog, index in enumerate(indices, 1):
        grid = im.crop(index)
        grid_rgb = mean_img_rgb(grid)
        # file_name = images[screening(grid_rgb,l)[1]]
        file_name = images[compare1(grid_rgb, l)[1]]
        # piece = Image.new('RGB', (64, 64), grid_rgb)
        piece = Image.open(f'./pic/{q}/'+file_name)
        if piece.mode != 'RGB':
            piece = piece.convert('RGB')
        #print(file_name)
        piece_resize = piece.resize(pix)
        piece_boost = boost_color(piece_resize, grid_rgb)
        #im.paste(piece_resize, index[:2])
        im.paste(piece_boost, index[:2])
        # print(grid_rgb)
        # print()
        print(f"{prog}/{comp}", end="\r")
    im.show()
    im.close()
    toc = time.process_time()
    print(toc - tic)
