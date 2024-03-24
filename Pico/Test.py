from neopixel import Neopixel
from ulab import numpy as np

ProgExec = 1

PixelNum = 296 #number of pixels
PixelWidth = 37 #how many pixels wide
PixelHight = 8 #how many pixels tall

PixelArr = np.arange(PixelNum).reshape((PixelHight, PixelWidth)) #creates an array of pixels with the proper dimensions

#defines neopixel object
pixels = Neopixel(PixelNum, 0, 0, "RGB") #Neopixel(number of LED's, state machine ID, GPIO number, mode(RGB or RGBW))

def ShowArt(art):
    artFileName = art + '_ARRAY.npy'
    artFile = open(artFileName, 'r')
    artArr = np.load(artFileName, dtype=object)
    print(artArr)
    for i in range(PixelHight):
        for j in range(PixelWidth):
            pixels.set_pixel(PixelArr[i][j], (artArr[i][j][0], artArr[i][j][1], artArr[i][j][2]))
    pixels.show()

if ProgExec == 1:
    ShowArt('HAT_ART')
