import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(0), 4)

np[0] = (35,44,0)
np[1] = (55,0,100)

np.write()