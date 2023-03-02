import numpy as np

arr = np.random.randint(0, 10, size=(3, 4))
arr2 = arr.copy()

print("Array:")
print(arr)
print()

print("Sort by 0 axis ('y'):")
arr.sort(axis=0)
print(arr)
print()

print("Sort by 1 axis ('y'):")
arr2.sort(axis=1)
print(arr2)