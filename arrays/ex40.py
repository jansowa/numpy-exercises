import numpy as np

arr = np.ones(shape=(3, 5), dtype=int) * 2
print(arr)

arr2 = np.full((3, 5), 2, dtype=int)
print(arr2)

arr3 = np.array([2])
arr3 = np.tile(arr3, (3, 5))
print(arr3)