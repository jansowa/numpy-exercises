import numpy as np

arr1 = np.random.randint(0, 2, 2)
arr2 = np.random.randint(0, 2, 2)
print("Array 1: ", arr1)
print("Array 2: ", arr2)
print("Are arrays equal? ", np.array_equal(arr1, arr2))
