import numpy as np

arr1 = np.array([[1, 2],
                [0, 3]])

arr2 = np.array([[0, 1],
                [0, 1]])

arr3 = np.array([[1, 2],
                [3, 4]])

print(np.any(arr1, axis=0))
print(np.any(arr1, axis=1))

print(np.any(arr2, axis=0))
print(np.any(arr2, axis=1))

print(arr1[0, 1])

print(np.any(arr3, axis=0))
print(np.any(arr3, axis=1))
