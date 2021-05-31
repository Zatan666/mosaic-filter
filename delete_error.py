from PIL import Image
import os

q = 'forest'
path = f'pic/{q}/'
files = os.listdir(path)
files.sort(key=lambda x: int(x.split('.')[0]))

for i in files:
    try:
        img = Image.open(path + i)
    except:
        print(i, 'deleting ...')
        os.remove(path + i)
