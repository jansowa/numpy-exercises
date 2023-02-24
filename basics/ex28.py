import numpy as np

array = np.zeros((10, 10))
array[0, :] = 1
array[-1, :] = 1
array[:, 0] = 1
array[:, -1] = 1
print(array)


array2 = np.ones((10, 10))
array2[1:-1, 1:-1] = 0
print(array2)

print(np.array_equal(array, array2))