#!/usr/bin/python

from PIL import Image
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from coloring import boost_color, alpha_color
from compare import list_mean_rgb,compare1
import time
import os
from itertools import cycle

if __name__ == '__main__':
    tic = time.process_time()
    q = 'forest'
    pix = (16, 16)
    select = 373
    print(f'open {q} {select}.jpg ...')
    im = Image.open(f'pic/{q}/{select}.jpg')
    im = im.convert('RGBA')
    path = f'pic/{q}/'
    files = os.listdir(path)
    files.sort(key=lambda x: int(x.split('.')[0]))

    indices = pixels_by_size(im, pix)

    comp = len(indices)
    for prog, (index, file_name) in enumerate(zip(indices, cycle(files)), 1):

        piece = Image.open(f'./pic/{q}/'+file_name)
        if piece.mode != 'RGBA':
            piece = piece.convert('RGBA')

        piece_resize = piece.resize(pix)
        piece_boost = alpha_color(piece_resize, 69)

        im.paste(piece_boost, index[:2], piece_boost)

        print(f"{prog}/{comp}", end="\r")
    im.show()
    im.close()
    toc = time.process_time()
    print(toc - tic)
