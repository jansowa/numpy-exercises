import numpy as np

array = np.array([1, 2, 3])

path1 = "ex35file"
array.tofile(path1)
dt = array.dtype
loaded_array = np.fromfile(path1, dtype=dt)
print(loaded_array)

path2 = "ex35file2.npy"
np.save(path2, array)
loaded_array2 = np.load(path2)
print(loaded_array2)
