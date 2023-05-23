import numpy as np

arr1 = np.array([[1, 2, 3],
                [4, 5, 6]])

arr2 = np.array([[1, 2],
                [3, 4],
                [5, 6]])

print(np.matmul(arr1, arr2))
print(np.dot(arr1, arr2))
print(arr1.dot(arr2))
