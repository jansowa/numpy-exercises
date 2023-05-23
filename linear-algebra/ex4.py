import numpy as np

arr = np.random.randint(0, 10, (3, 3))
print("Matrix:")
print(arr)
print()

print("Matrix determinant:")
print(np.linalg.det(arr))
