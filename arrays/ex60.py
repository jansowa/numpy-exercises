import numpy as np

arr1 = np.array([[1], [2], [3]])
arr2 = np.array([[4], [5], [6]])

print(np.dstack([arr1, arr2]))
print(np.concatenate([arr1, arr2], axis=1).reshape((3, 1, 2)))