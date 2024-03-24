from neopixel import Neopixel
from ulab import numpy as np
import machine, time
import rp2

ProgExec = 1

PixelNum = 296 #number of pixels
PixelWidth = 37 #how many pixels wide
PixelHight = 8 #how many pixels tall

PixelArr = np.arange(PixelNum).reshape((PixelHight, PixelWidth)) #creates an array of pixels with the proper dimensions

#defines neopixel object
pixels = Neopixel(PixelNum, 0, 0, "GRB") #Neopixel(number of LED's, state machine ID, GPIO number, mode(RGB or RGBW))

def ShowArt(art):
    artFileName = art + '_ARRAY.npy'
    #artFile = open(artFileName, 'r')
    #print(artFile)
    artArr = np.load(artFileName)
    print('yay')
    for i in range(PixelHight):
        for j in range(PixelWidth):
            pixels.set_pixel(PixelArr[i][j], (artArr[i][j][0], artArr[i][j][1], artArr[i][j][2]))
    pixels.show()

def TestSwirl():
    for i in range(0, PixelNum):
        pixels.set_pixel(i, (85, 85, 85))
        pixels.set_pixel(i-8, (0, 0, 0))
        time.sleep(.1)
        pixels.show()

#FIRST logo and team number
if ProgExec == 1:
    ShowArt('HAT_ART')

#run through 8 at a time white (to see if larger strips are calibrated without having to power  all at once)
if ProgExec == 2:
    TestSwirl()