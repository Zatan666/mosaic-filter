from mean_rgb_values import mean_img_rgb
from PIL import Image

def compare1(img1: Image, img2:Image):
    mean1 = mean_img_rgb(img1)
    mean2 = mean_img_rgb(img2)
    values = [abs(i - j) for i, j in zip(mean1, mean2)]
    diff = sum(values)
    return diff


if __name__ == '__main__':
    img1 = Image.open('./pic/test.png')
    img2 = Image.open('./pic/test.png')
    diff = compare1(img1, img2)
    print(diff)
    img1.close()
    img2.close()
