import numpy as np

array = np.array([1, 2, 3])

path1 = "ex37file.txt"
array.tofile(path1, sep=",")
dt = array.dtype
print("Array to save:")
print(array)
loaded_array = np.fromfile(path1, dtype=dt, sep=",")
print("Loaded array:")
print(loaded_array)

print("Are arrays equal: " + str(np.array_equal(array, loaded_array)))

path2 = "ex37file2.txt"
np.savetxt(path2, array)

loaded_array2 = np.loadtxt(path2)
print("Array loaded in the second way:")
print(loaded_array2)
print("Are arrays equals: " + str(np.array_equal(array, loaded_array2)))
