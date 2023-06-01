import numpy as np

arr = np.arange(10)
arr2 = np.random.randint(1, 10, 10)

print("array: " + str(arr))
print("array 2: " + str(arr2))

print(np.true_divide(arr, arr2))
print(arr / arr2)
print(np.divide(arr, arr2))