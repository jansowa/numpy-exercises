import numpy as np

arr = np.array([1, 2, 3, 4])

print(np.array(arr.tolist() * 3))
print(np.tile(arr, 3))
