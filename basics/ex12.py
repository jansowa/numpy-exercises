import numpy as np
from sys import getsizeof

x = np.array([1, 7, 13, 105])

print("Size of the whole object: " + str(getsizeof(x)))
print("Size of the array elements: " + str(x.nbytes))
print("Size of the array elements: " + str(x.size * x.itemsize))
