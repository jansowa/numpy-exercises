import numpy as np

arr = np.random.randint(1, 100, size=(3, 4), dtype=int)
arr2 = np.random.randint(1, 100, size=(3, 4), dtype=int)

print("Array:")
print(arr)

arr.sort(axis=0)
print("Sorted along axis 0 ('y'):")
print(arr)

arr2.sort(axis=1)
print("Sorted along axis 1 ('x'):")
print(arr2)
