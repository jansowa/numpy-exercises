import numpy as np

arr = np.arange(0, 50, 2)
print(np.isin([1, 16, 17, 48, 51], arr))

print()

print(1 in arr)
print(16 in arr)
print(17 in arr)
print(48 in arr)
print(51 in arr)