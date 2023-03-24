import numpy as np

arr = np.random.random((3, 3))
print("Array:")
print(arr)
print()

xmin, xmax = np.min(arr), np.max(arr)
print("Normalized array:")
print((arr - xmin)/(xmax - xmin))
