import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Array: ", arr)
print("Max element index: ", arr.argmax())
print("Min element index: ", arr.argmin())

arr2 = np.random.randint(0, 100, size=(3, 4))
print("Array 2:")
print(arr2)
print("Max element index (axis 0): ", arr2.argmax(axis=0))
print("Max element index (axis 1): ", arr2.argmax(axis=1))

print("Min element index (axis 0): ", arr2.argmin(axis=0))
print("Min element index (axis 0): ", arr2.argmin(axis=1))
