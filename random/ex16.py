import numpy as np

n=3
arr = np.random.randint(0, 100, 100)
arr.sort()
print(arr[-n:])

arr = np.random.randint(0, 100, 100)
print(arr[np.argsort(arr)[-n:]])