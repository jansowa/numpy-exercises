import numpy as np

arr = np.arange(16).reshape((4, 4))
print(arr)

print(np.split(arr, [2], axis=1))
print(np.hsplit(arr, [2]))