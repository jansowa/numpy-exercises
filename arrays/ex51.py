import numpy as np

arr = np.array([[1, 2, 3]])

print(arr.reshape((3, 1)))
print(arr.swapaxes(0, 1))