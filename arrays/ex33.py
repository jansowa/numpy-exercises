import numpy as np
import sys

arr = np.random.random(size=(3, 4))


print("Size of single element in bytes:")
print(arr.itemsize)

print("Summary size of all elements:")
print(arr.size * arr.itemsize)

print("Array size in bytes:")
print(sys.getsizeof(arr))
