import numpy as np

arr = np.random.random((2, 3))

print("Array:\n" + str(arr))

print("fortran order:")
for x in np.nditer(arr, order='F'):
    print(x)
