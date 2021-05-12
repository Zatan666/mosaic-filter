

'''
#grid_rgb

for i in range(width_grid):
    for j in range(height_grid):
        r,g,b = grid.getpixel((i,j))
        mean_grid = (r+g+b)/3


'''

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
