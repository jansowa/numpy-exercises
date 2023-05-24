import numpy as np

arr1, arr2 = [[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
print("arr1:")
print(arr1)
print("arr2:")
print(arr2)

print("concatenate:")
print(np.concatenate((arr1, arr2), axis=1))