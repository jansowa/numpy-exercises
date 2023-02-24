import numpy as np

arr = np.array([1, 2, 3, 4, 5])
dt = arr.dtype

print("Array before converting to bytes:")
print(arr)
arrbytes = arr.tobytes()
arr2 = np.frombuffer(arrbytes, dtype=dt)
print(arr2)
print("Are arrays equal: " + np.equal(arr, arr2))
