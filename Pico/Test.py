from neopixel import Neopixel
import numpy as np

PixelNum = 296 #number of pixels
PixelWidth = 37 #how many pixels wide
PixelHight = 8 #how many pixels tall

PixelArr = np.arange(PixelNum).reshape(PixelHight, PixelWidth) #creates an array of pixels with the proper dimensions

#defines neopixel object
pixels = Neopixel(PixelNum, 0, 0, "RGB") #Neopixel(number of LED's, state machine ID, GPIO number, mode(RGB or RGBW))

pixels.show() #shows the pixels

def ShowArt(art):
    for i in range(PixelNum):
