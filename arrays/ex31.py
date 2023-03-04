import numpy as np

arr = np.array([[0, 10, 20],
                [20, 30, 40]])

print("Array:")
print(arr)
print()

print("Values greater than 10:")
print(arr[arr>10])
print()

print("Indexes of values greater than 10:")
print(np.where(arr>10))