from mean_rgb_values import mean_img_rgb
from indices import pixels_by_size
from mean_rgb_values import mean_img_rgb
from PIL import Image
import os

def compare1(grid_rgb: ('r','g','b'), list_rgb:[('r','g','b')]):
    diffs = [sum(abs(i - j) for i, j in zip(grid_rgb, rgb))
                            for rgb in list_rgb]
    min_diff = min(diffs)
    min_index = diffs.index(min_diff)
    min_img = list_rgb[min_index]
    return min_img, min_index

def list_mean_rgb(q: 'search' = None):
    if q is None:
        path = 'pic/'
        files = os.listdir(path)
        files = [i for i in files if i.endswith('.png')]
        files.remove('test.png')
    else:
        path = f'pic/{q}/'
        files = os.listdir(path)

    list_mean = []
    for i in files:
        img = Image.open(path + i)
        list_mean.append(mean_img_rgb(img))
        img.close()
    return list_mean

def screening(grid_rgb,pieces_rgb):
    r_screen = []
    g_screen = []
    b_screen = []

    for piece_rgb in pieces_rgb:

        if piece_rgb[0] in range(grid_rgb[0]-10,grid_rgb[0]+10+1):
            r_screen.append(piece_rgb)

        for piece_rgb in r_screen:
            if piece_rgb[1] in range(grid_rgb[1]-10,grid_rgb[1]+10+1):
                g_screen.append(piece_rgb)

        for piece_rgb in g_screen:
            if piece_rgb[2] in range(grid_rgb[2]-10,grid_rgb[2]+10+1):
                b_screen.append(piece_rgb)

    if len(b_screen) > 1:
        diff = []
        for piece_rgb in b_screen:
            diff.append(grid_rgb - piece_rgb)
            min_diff = min(diff)
            min_index = diff.index(min_diff)
            min_pieces = pieces_rgb[min_index]
            return min_pieces, min_index
    else:
        return piece_rgb, pieces_rgb.index(piece_rgb)


from os import listdir
images = listdir('./pic/')

if __name__ == '__main__':
    im = Image.open('./pic/test.png')
    indices = pixels_by_size(im, (64, 64))
    print('number of grid by size 64x64', len(indices))
    for index in indices[:5]:
        grid = im.crop(index)
        grid_rgb = mean_img_rgb(grid)
        piece1 = images[screening(grid_rgb,list_mean_rgb())[1]]
        # piece = Image.new('RGB', (64, 64), grid_rgb)
        piece = Image.open('./pic/'+piece1)
        im.paste(piece, index[:2])

    im.show()
    im.close()



