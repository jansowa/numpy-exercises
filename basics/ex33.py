import numpy as np

arr1 = np.arange(1, 4)
arr2 = np.arange(3, 0, -1)
print("Vector 1: " + str(arr1))
print("Vector 2: " + str(arr2))

print(np.dot(arr1, arr2))
print(np.sum(arr1 * arr2))