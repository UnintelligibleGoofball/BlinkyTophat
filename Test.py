from neopixel import Neopixel

pixels = Neopixel(10, 0, 0, "RGB")

pixels.fill((100,0,150))

pixels.show()