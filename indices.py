from PIL import Image
from fractions import Fraction
from math import ceil, sqrt

def pixels_by_size(image: Image, size: "(Width, Height)") -> list:
    """
    give pixels index of each grid by input of size
    """
    x_step, y_step = size
    indices = [(i, j, min(i+x_step, image.width), min(j+y_step, image.width))
               for i in range(0, image.width, x_step)
               for j in range(0, image.height, y_step)]
    return indices


def pixels_by_num(image: Image, num: int) -> list:
    """
    give pixels index of each grid by input of grid number (change to closest n^2)
    """
    num = round(sqrt(num))
    nearest_sq = num ** 2
    
    x_step, y_step = [round(size / num) for size in image.size]
    indices = [(i, j, i+x_step-1, j+y_step-1) for i in range(0, image.width, x_step)
                                              for j in range(0, image.height, y_step)]

    return indices


def dimention(image: Image) -> (int, int):
    """
    give respect ratio of this image
    """
    di = Fraction(*image.size).limit_denominator(100)
    return di.numerator, di.denominator


if __name__ == '__main__':
    im = Image.open('./pic/test.png')
    indices = pixels_by_size(im, (64, 64))
    print('number of grid by size 64x64', len(indices))
    indices = pixels_by_num(im, 117)
    print('number of grid by num 117', len(indices))
    # sample = Image.new('RGB', (10, 10), (0, 0, 0))
    # for index in indices:
    #     im.paste(sample, index)
    # im.show()
    im.close()
