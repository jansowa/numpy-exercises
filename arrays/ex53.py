import numpy as np

arr = np.zeros((2, 3, 4, 5))
print(arr.shape)

print(np.moveaxis(arr, -1, 1).shape)