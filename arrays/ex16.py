import numpy as np
import sys

arr = np.random.random((3, 4))

arr2 = np.array([1, 2, 3, 4])

print("Number of array elements: ", str(arr.size))
print("Size of single element: ", str(arr.itemsize))
print("Size of all elements: ", str(arr.nbytes))
print("Size of the whole array: ", str(sys.getsizeof(arr)))
