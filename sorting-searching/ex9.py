import numpy as np

arr = np.array([[1, 5, 0],
                [3, 2, 5],
                [8, 7, 6]])
print(arr[arr[:, 1].argsort()])
