import numpy as np

arr = np.random.random((3, 4))
print("Array: ")
print(arr)

print("Filled with 0:")
arr[:] = 0
print(arr)

arr2 = np.random.random((4, 3))
print("Array:")
print(arr2)
print("Filled with 0:")
print(np.zeros_like(arr2))
