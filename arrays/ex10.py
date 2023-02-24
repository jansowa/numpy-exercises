import numpy as np

arr = np.zeros((8, 8))

arr[::2, 1::2] = 1
arr[1::2, ::2] = 1

print(arr)

square = np.array([0, 1, 1, 0]).reshape(2, 2)
arr2 = np.tile(square, (4, 4))

print(arr2)
