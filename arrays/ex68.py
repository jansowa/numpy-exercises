import numpy as np

# Method 1
multiple5 = np.arange(5, 100, 5)
multiple3 = np.arange(3, 100, 3)
arr = np.unique(
            np.concatenate(
                [multiple5, multiple3]))
print(arr.sum())

# Method 2
arr = np.arange(1, 100)
print(arr[(arr % 3 == 0) | (arr % 5 == 0)].sum())