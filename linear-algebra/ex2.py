import numpy as np

arr1 = np.random.randint(0, 10, (4, 1))
arr2 = np.random.randint(0, 10, (4, 1))

print("Array 1:")
print(arr1)
print()

print("Array 2:")
print(arr2)
print()

print("Outer product:")
print(arr1.dot(arr2.T))

print()
print(np.outer(arr1, arr2))
