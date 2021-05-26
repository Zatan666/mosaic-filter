from PIL import Image

im = Image.open('./pic/test.png')
im.show()
colors = (99, 138, 23)
factor = tuple(i / 255 for i in colors)
for i in range(im.width):
    for j in range(im.height):
        rgb = im.getpixel((i, j))
        im.putpixel((i, j), tuple(int(x * c) for x, c in zip(rgb, factor)))
im.show()
im.close()