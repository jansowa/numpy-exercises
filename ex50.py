import numpy as np

arr1 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print(arr1)

tmp = arr1[0]
arr1[0] = arr1[3]
arr1[3] = tmp
print(arr1)

arr2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print(arr2)
arr2[[0, -1]] = arr2[[-1, 0]]
print(arr2)