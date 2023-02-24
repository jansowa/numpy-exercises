import numpy as np

arr1 = np.random.randint(0, 5, size=(2, 3))
arr2 = np.random.randint(0, 5, size=(2, 3))

print("Array 1:")
print(arr1)

print("Array 2:")
print(arr2)

print("Multiplication element by element:")
print(arr1 * arr2)
print(np.multiply(arr1, arr2))