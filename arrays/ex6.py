import numpy as np

arr = np.arange(12, 38)
print("Array before flip: ", str(arr))
print("Array after flip: ", str(np.flip(arr)))
print("Array after flip: ", str(arr[::-1]))
