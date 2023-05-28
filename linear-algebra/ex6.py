import numpy as np

arr1 = np.random.randint(1, 10, 5)
print("array 1: " + str(arr1))

arr2 = np.random.randint(1, 10, 5)
print("array 2: " + str(arr2))

print("Inner product: " + str(np.inner(arr1, arr2)))

arr3 = np.random.randint(1, 10, (2, 3))
print("array 3:\n" + str(arr3))

arr4 = np.random.randint(1, 10, (2, 3))
print("array 4:\n" + str(arr4))

print("Inner product: " + str(np.inner(arr3, arr4)))
