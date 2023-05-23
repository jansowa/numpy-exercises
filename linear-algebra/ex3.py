import numpy as np

arr1 = np.random.randint(0, 10, (2, 2))
arr2 = np.random.randint(0, 10, (2, 2))

print("First matrix:")
print(arr1)
print()

print("Second matrix:")
print(arr2)
print()

print("Cross product:")
print(np.cross(arr1, arr2))
