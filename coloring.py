from PIL import Image

def boost_color(im: Image, color: (int, int, int)):
    factor = tuple(i / 128 for i in color)
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
    im = Image.open('./pic/test.png')
    im.show()
    # boost color
    #color = (99, 138, 23)
    #im_boost = boost_color(im, color)
    #im_boost.show()
    #im_boost.close()
    im_alpha = alpha_color(im, 100)
    im_alpha.show()
    im_alpha.close()
    im.close()
