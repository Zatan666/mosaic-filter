from PIL import Image
from mean_rgb_values import mean_img_rgb

def boost_color(im: Image, color: (int, int, int)):
    factor = tuple(i / j for i, j in zip(color, mean_img_rgb(im)))
    for i in range(im.width):
        for j in range(im.height):
            rgb = im.getpixel((i, j))
            #print(im.mode, rgb)
            im.putpixel((i, j), tuple(map(lambda x: int(x[0] * x[1]), zip(rgb, factor))))
    return im


def alpha_color(im: Image, alpha: int=100):
    r, g, b, a = im.split()
    a.putdata([(alpha)] * (a.width * a.height))
    merge = Image.merge('RGBA', (r, g, b, a))
    return merge


if __name__ == '__main__':
    im = Image.open('bright.jpg')
    im.show()
    # boost color
    color = (128, 128, 128)
    im_boost = boost_color(im, color)
    #im_boost = alpha_color(im, 100)
    im_boost.show()
    im_boost.close()
    im.close()
