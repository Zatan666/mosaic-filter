from PIL import Image
from fractions import Fraction
from math import ceil, sqrt

def pixels_by_size(image: Image, size: "(Width, Height)") -> list:
    """
    give pixels index of each grid by input of size
    """
    x_step, y_step = size
    indices = [(i, j, min(i+x_step, image.width), min(j+y_step, image.height))
               for i in range(0, image.width, x_step)
               for j in range(0, image.height, y_step)]
    return indices


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
