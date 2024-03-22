#neopixel library thats kinda jank but works better than the normal one
from neopixel import Neopixel

#defines neopixel object
#Neopixel(number of LED's, state machine ID, GPIO number, mode(RGB or RGBW))
pixels = Neopixel(10, 0, 0, "RGB")

pixels.fill((100,0,150)) #every defined pixel set to a light blue

pixels.show() #shows the pixels