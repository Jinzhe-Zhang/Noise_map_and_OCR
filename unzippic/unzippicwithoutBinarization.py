from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
WIDTH=1280
HEIGHT=960
RANGE=7
m=16
def func(i):
def color(i,j,rangee):
    ary=[]
    for ii in range(i-rangee,i+rangee+1):
        for jj in range(j-rangee,j+rangee+1):
            if 0<=ii<WIDTH and 0<=jj<HEIGHT:
                ary.append((ii,jj))
    return ary
def avg(a):
    b=[0 for _ in range(len(a[0]))]
    for i in a:
        for j in range(len(i)):
            b[j]+=i[j]
    for i in range(len(b)):
        b[i]//=len(a)
    return tuple(b)
image = Image.open('pic.png')
image2 = Image.new('RGB',(WIDTH,HEIGHT))
for i in range(image.size[0]):
    for j in range(image.size[1]):
        image2.putpixel((i,j),avg(list(map(lambda x:image.getpixel(x),color(i,j,RANGE)))))
image2.save(open('newpic.png','wb'),'png')