import numpy as np

array = np.array([0, 1] * 8).reshape((4, 4))
array[1] = np.flip(array[1])
array[3] = np.flip(array[3])
print(array)

array2 = np.zeros((4, 4))
array2[1::2, ::2] = 1
array2[::2, 1::2] = 1
print(np.array_equal(array, array2))
