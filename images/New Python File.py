from PIL import Image
import os


def convert_quality(path,dest,quality=70,grayscale=False):
    foo = Image.open(path)
    if grayscale == True:
        foo = foo.convert('L')
    x = int(foo.size[0]*(quality/100))
    y = int(foo.size[1]*(quality/100))
    foo = foo.resize((x,y),Image.ANTIALIAS)
    foo.save(dest,optimize=True,quality=quality)


i = 'bg_1.png'
convert_quality(i,i,70)