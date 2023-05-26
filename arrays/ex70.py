import numpy as np

arr = np.random.random((3, 4))

# Method 1
for x in arr.flatten():
    print(x)

# Method 2
for x in np.nditer(arr):
    print(x)
