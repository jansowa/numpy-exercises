import numpy as np

size = int(input("Enter size (single number): "))

arr = np.ones((size, size))
arr[1:-1, 1:-1] = 0
print(arr)

arr2 = np.zeros((size, size))
arr2[[0, -1], :] = 1
arr2[:, [0, -1]] = 1
print(arr2)