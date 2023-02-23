import numpy as np

arr = np.random.randint(0, 10, (4, 4))
print("Array:")
print(arr)

print("Array after transformation:")
print(np.flip(arr, axis=1))
arr[:, [0, 1, 2, 3]] = arr[:, [3, 2, 1, 0]]
print(arr)