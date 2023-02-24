import numpy as np

array = np.zeros((5, 5))

for k in range(5):
    array[k, k] = k+1

print(array)

array2 = np.identity(5) * np.arange(1, 6)
array3 = np.diag(np.arange(1, 6))
array4 = np.zeros((5, 5))
array4[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] = np.arange(1, 6)

print(np.array_equal(array, array2))
print(np.array_equal(array, array3))
print(np.array_equal(array, array4))
