import os

from PIL import Image as img


def circleBres(xc,yc,r)  :
    im = img.new(mode='1', size=(1000,1000),color=1)
    x,y = 0,r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y,im)
    while (y >= x):
        # // for each pixel we will
        # // draw all eight pixels

        x+=1

        #  check for decision parameter
        #  and correspondingly
        #  update d, x, y
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10

        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y,im)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,"circle.png")
    im.show()
    im.save(fp=file_path)

def drawCircle(xc, yc ,x, y,im):

    im.putpixel((xc+x, yc+y), 0)
    im.putpixel((xc-x, yc+y), 0)
    im.putpixel((xc+x, yc-y), 0)
    im.putpixel((xc-x, yc-y), 0)
    im.putpixel((xc+y, yc+x), 0)
    im.putpixel((xc-y, yc+x), 0)
    im.putpixel((xc+y, yc-x), 0)
    im.putpixel((xc-y, yc-x), 0)

