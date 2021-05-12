from PIL import Image
from fractions import Fraction

def get_grid_info(image: Image, size_grid: (int, int)) -> (int, (int, int)):
    # get (width, height) of image
    width, height = image.size
    # get ratio of grid
    dimention = Fraction(*image.size).limit_denominator(100)
    width_grid = size_grid[0] * dimention.numerator
    height_grid = size_grid[1] * dimention.denominator

    return num_grid, size_grid

if __name__ == '__main__':
    im = Image.open('./pic/test.png')
    print('size of image', im.size)
    num, size = get_grid_info(im, 10)
    im.close()
    print('number of grid:', num)
    print('size of each grid:', size)
