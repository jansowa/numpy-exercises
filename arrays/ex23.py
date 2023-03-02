import numpy as np

arr = np.array([0, 1, 2])
arr2 = np.array([1, 2, True, np.inf])

print(np.alltrue(arr))
print(np.alltrue(arr2))
