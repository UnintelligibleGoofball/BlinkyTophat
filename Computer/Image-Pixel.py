import numpy as np
from PIL import Image
img = Image.open('./Computer/HAT_ART.png')
arr = np.save('./Pico/Art/HAT_ART_ARRAY', img) # 37x8 array
checkarr = np.load('./Pico/Art/HAT_ART_ARRAY.npy')
print(checkarr)
