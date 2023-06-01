import numpy as np

arr = np.random.randint(1, 10, 10)
arr2 = np.random.randint(1, 10, 10)

print("array: " + str(arr))
print("array 2: " + str(arr2))

print(np.power(arr, arr2))
print(arr ** arr2)