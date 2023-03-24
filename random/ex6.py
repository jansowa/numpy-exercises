import numpy as np

arr = np.arange(10)
np.random.shuffle(arr)
print(arr)
print(np.random.permutation(np.arange(10)))