import numpy as np

arr = np.array([[10, 20, 30], [20, 40, 50]])

print("Array with shape (2, 3):")
print(arr)
print()

print("Array with shape (6,):")
print(arr.reshape((6, )))
print()

print("Array with shape (6,):")
arr.shape = (6,)
print(arr)