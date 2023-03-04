import numpy as np

arr = np.arange(1, 10)

print("Array with shape (9,):")
print(arr)
print()

print("Reshape to array with shape (3,3):")
print(arr.reshape((3, 3)))
print()

arr2 = np.arange(1, 10)
print("Array with shape (9,):")
print(arr2)

arr2.shape = (3, 3)
print("Array with shape (3, 3):")
print(arr2)