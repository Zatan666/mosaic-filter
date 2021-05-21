from mean_rgb_values import mean_img_rgb
from PIL import Image

def compare1(grid_rgb: ('r','g','b'), list_rgb:[('r','g','b')]):
    diffs = [sum(abs(i - j) for i, j in zip(grid_rgb, rgb))
                            for rgb in list_rgb]
    min_diff = min(diffs)
    min_index = diff.index(min_diff)
    min_img = list_img2[min_index]
    return min_img, min_index

def list_mean_rgb(list_img:[Image]):
    list_mean = [mean_img_rgb(i) for i in list_img]
    return list_mean

if __name__ == '__main__':
    pass
