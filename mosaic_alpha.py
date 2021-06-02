#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from coloring import boost_color, alpha_color
from compare import list_mean_rgb,compare1,screening
import time
import os

if __name__ == '__main__':
    tic = time.process_time()
    q = 'forest'
    pix = (48, 48)
    select = 475
    print(f'open {q} {select}.jpg ...')
    im = Image.open(f'pic/{q}/{select}.jpg')
    im = im.convert('RGBA')
    print('open and cal rgb other pic ...')
    #images, l = list_mean_rgb(q, pix, select)
    path = f'pic/{q}/'
    files = os.listdir(path)
    files.sort(key=lambda x: int(x.split('.')[0]))
    # print(im.size, '\n')
    indices = pixels_by_size(im, pix)
    # print('number of grid by size 64x64', len(indices))
    comp = len(indices)
    for prog, (index, piece1) in enumerate(zip(indices, files), 1):
        #grid = im.crop(index)
        #grid_rgb = mean_img_rgb(grid)
        # piece1 = images[screening(grid_rgb,l)[1]]
        #piece1 = images[compare1(grid_rgb, l)[1]]
        # piece = Image.new('RGB', (64, 64), grid_rgb)
        piece = Image.open(f'./pic/{q}/'+piece1)
        if piece.mode != 'RGBA':
            piece = piece.convert('RGBA')
        #print(piece1)
        piece_resize = piece.resize(pix)
        piece_boost = alpha_color(piece_resize, 69)
        #im.paste(piece_resize, index[:2])
        im.paste(piece_boost, index[:2], piece_boost)
        # print(grid_rgb)
        # print()
        print(f"{prog}/{comp}", end="\r")
    im.show()
    im.close()
    toc = time.process_time()
    print(toc - tic)
