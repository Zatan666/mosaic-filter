from mean_rgb_values import mean_img_rgb
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from PIL import Image
import os
import numpy

def compare1(grid_rgb: (int, int, int), list_rgb:[(int, int, int)]):
    diffs = [sum(abs(i - j) for i, j in zip(grid_rgb, rgb))
                            for rgb in list_rgb]
    min_diff = min(diffs)
    min_index = diffs.index(min_diff)
    min_img = list_rgb[min_index]
    return min_img, min_index

def list_mean_rgb(q: 'search' = None, pix: (int, int) = (32, 32), select: int = 1):
    if q is None:
        path = 'pic/doom+game/'
        files = os.listdir(path)
        files.sort(key=lambda x: int(x.split('.')[0]))

    else:
        path = f'pic/{q}/'
        files = os.listdir(path)
        files.sort(key=lambda x: int(x.split('.')[0]))

    list_mean = []
    for i in files:
        print(i, end='\r')
        img = Image.open(path + i)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize(pix)
        list_mean.append(mean_img_rgb(img))
        img.close()
    print('list *ALL* rgb values complete')
    return files, list_mean


if __name__ == '__main__':
    im = Image.open('./pic/test.png')
    # print(im.size, '\n')
    indices = pixels_by_size(im, (64, 64))
    # print('number of grid by size 64x64', len(indices))
    images, l = list_mean_rgb()
    for index in indices:
        # print(index)
        grid = im.crop(index)
        grid_rgb = mean_img_rgb(grid)
        # piece1 = images[screening(grid_rgb,l)[1]]
        piece1 = images[compare1(grid_rgb, l)[1]]
        # piece = Image.new('RGB', (64, 64), grid_rgb)
        piece = Image.open('./pic/'+piece1)
        im.paste(piece, index[:2])
        # print(grid_rgb)
        # print()
    im.show()
    im.close()
