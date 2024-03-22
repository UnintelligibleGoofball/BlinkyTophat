import numpy as np
from PIL import Image
img = Image.open('lena.png')
arr = np.array(img) # 640x480x4 array
arr[20, 30] # 4-vector, just like above