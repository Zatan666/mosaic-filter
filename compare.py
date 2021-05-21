from mean_rgb_values import mean_img_rgb
from PIL import Image
import os

def compare1(grid_rgb: ('r','g','b'), list_rgb:[('r','g','b')]):
    diffs = [sum(abs(i - j) for i, j in zip(grid_rgb, rgb))
                            for rgb in list_rgb]
    min_diff = min(diffs)
    min_index = diff.index(min_diff)
    min_img = list_img2[min_index]
    return min_img, min_index

def list_mean_rgb(q: 'search'):
    path = f'pic/{q}/'
    files = os.listdir(path)
    files = [i for i in files if i.endswith('.png')]
    list_mean = []
    for i in files:
        img = Image.open(path + i)
        list_mean.append(mean_img_rgb(img))
        img.close()
    return list_mean

if __name__ == '__main__':
    pass
