import numpy as np

arr = np.random.random((3, 4))

print("Array to save:")
print(arr)

path = "ex36.npz"
np.savez_compressed(path, arr=arr)
arr_loaded = np.load(path)["arr"]
print("Loaded array:")
print(arr_loaded)

print("Are arrays equal: " + str(np.array_equal(arr, arr_loaded)))
