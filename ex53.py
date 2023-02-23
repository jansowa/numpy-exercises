import numpy as np

arr = np.random.randint(100, size=10)

print("Array:")
print(arr)

mean = np.mean(arr)

print("Elements higher than ", str(mean), ":")
print(arr[arr > mean])

print("Elements lower than ", str(mean), ":")
print(arr[arr < mean])
