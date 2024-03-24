import numpy as np
from PIL import Image
img = Image.open('./Computer/HAT_ART.png')
arr = np.save('./Pico/Art/HAT_ART_ARRAY', img) # 37x8 array

