#grid_rgb

from PIL import Image



main = Image.open("./pic/test.png")
width_main,height_main =  main.size
width_grid = width_main//24
height_grid = height_main//24


a = Image.new('RGB',(width_grid, height_grid),(0,0,0))

red = []
green = []
blue = []

for i in range(0,width_grid):
    for j in range(0,height_grid):
        r,g,b = main.getpixel((i,j))
        a.putpixel((i,j),(r,g,b))
        red.append(r)
        green.append(g)
        blue.append(b)
        sum_red = round(sum(red)/(width_grid*height_grid))
        sum_green = round(sum(green)/(width_grid*height_grid))
        sum_blue = round(sum(blue)/(width_grid*height_grid))
        mean_grid = sum_red,sum_green,sum_blue





#piece_rgb

from PIL import Image

piece = Image.open("./pic/test.png")

width_piece,height_piece =  piece.size

red = []
green = []
blue = []

for i in range(width_piece):
    for j in range(height_piece):
        r,g,b = piece.getpixel((i,j))
        red.append(r)
        green.append(g)
        blue.append(b)


sum_red = round(sum(red)/(width_piece*height_piece))
sum_green = round(sum(green)/(width_piece*height_piece))
sum_blue = round(sum(blue)/(width_piece*height_piece))

mean_piece = sum_red,sum_green,sum_blue
print(mean_piece)

