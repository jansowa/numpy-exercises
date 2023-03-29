import numpy as np

arr = np.random.randint(0, 10, (2, 3, 4))

print("Array shape: ", arr.shape)
print("Array:")
print(arr)
print()


arr2 = np.moveaxis(arr, 0, -1)
print("Array shape: ", arr2.shape)
print("Array:")
print(arr2)
print()

arr3 = np.moveaxis(arr, -1, 0)
print("Array shape: ", arr3.shape)
print("Array:")
print(arr3)
