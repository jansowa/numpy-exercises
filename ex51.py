import numpy as np

type = int

arr = np.zeros((5, 6), dtype=type)
print(arr)

arr[::2, ::2] = 3
arr[1::2, ::2] = 7
print(arr)
