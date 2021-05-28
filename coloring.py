from PIL import Image

def boost_color(im: Image, color: (int, int, int)):
    factor = tuple(i / 255 for i in color)
    for i in range(im.width):
        for j in range(im.height):
            rgb = im.getpixel((i, j))
            print(rgb, factor)
            im.putpixel((i, j), tuple(map(lambda x: int(x[0] * x[1]), zip(rgb, factor))))
    return im

if __name__ == '__main__':
    im = Image.open('./pic/test.png')
    im.show()
    color = (99, 138, 23)
    im_boost = boost_color(im, color)
    im_boost.show()
    im.close()
    im_boost.close()
