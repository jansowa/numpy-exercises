import numpy as np

width = int(input("Enter array width: "))
height = int(input("Enter array height: "))

arr = np.arange(width * height).reshape((height, width))

print(np.pad(arr, 1))
