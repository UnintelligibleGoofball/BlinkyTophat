import numpy as np
from PIL import Image
img = Image.open('./Computer/HAT_ART.png')
arr = np.array(img) # 37x8 array

# Program to save a NumPy array to a text file

# Displaying the array
print('Array:\n', arr)
file = open("./Pico/Art/HAT_ART_ARRAY.txt", "w+")

# Saving the array in a text file
content = str(arr)
file.write(content)
file.close()
