import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

print(np.array([arr1, arr2]).T)
print(np.column_stack((arr1, arr2)))