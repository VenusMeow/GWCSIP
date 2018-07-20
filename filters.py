#imports image sub-module from pillow module
from PIL import Image

#opens file using a given filename
def load_img(filename):
    im = Image.open(filename)
    return im

def obamicon(im):
    pixels = im.getdata()
    newpixels = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for p in pixels:
        intensity = sum(p)

        if intensity < 182:
            newpixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newpixels.append(red)
        elif intensity >= 364 and intensity < 546:
            newpixels.append(lightBlue)
        elif intensity >= 546:
            newpixels.append(yellow)

    newimage = Image.new("RGB",im.size)
    newimage.putdata(newpixels)
    return newimage

def grayscale(im):
    pixels = im.getdata()
    newpixels = []
    for p in pixels:
        total = sum(p)
        avg = total//3
        newpixels.append((avg,avg,avg))

    newim = Image.new("RGB",im.size)
    newim.putdata(newpixels)
    return newim

#display image to user
def show_img(im):
    im.show()

#saves image to your computer
def save_img(im,filename):
    im.save(filename, "jpeg")
    show_img(im)
