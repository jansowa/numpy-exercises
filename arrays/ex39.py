import numpy as np

arr = np.array([[2, 4, 6], [6, 8, 10]], dtype=np.int32)
print("Array:")
print(arr)
print("Data type of the array: ", arr.dtype)
print()

arr = arr.astype(dtype=np.float64)
print("Array:")
print(arr)
print("New data type of the array: ", arr.dtype)
