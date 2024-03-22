#neopixel library thats kinda jank but works better than the normal one
from neopixel import Neopixel

import machine, time

#
testPattern = 2
pixelCount = 10
#defines neopixel object
#Neopixel(number of LED's, state machine ID, GPIO number, mode(RGB or RGBW))
pixels = Neopixel(pixelCount, 0, 0, "GRB")

#show red, blue, and white next to eachother
if testPattern == 1:
    pixels.set_pixel(0, (0, 0, 255)) #set pixel 0 to blue
    pixels.set_pixel(1, (85, 85, 85)) #set pixel 1 to white
    pixels.set_pixel(2, (255, 0, 0)) #set pixel 2 to red

#set all pixels to white
if testPattern == 2:
    pixels.fill((85, 85, 85))

#run through 8 at a time white (to see if larger strips are calibrated without having to power  all at once)
if testPattern == 3:
    for i in range(0, pixelCount):
        pixels.set_pixel(i, (85, 85, 85))
        pixels.set_pixel(i-8, (0, 0, 0))
        time.sleep(.1)
        pixels.show()
 
pixels.show() #shows the pixels