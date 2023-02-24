import numpy as np


arr = np.arange(10)
print("Array: ", str(arr))

print("Replace numbers higher than 5: ", np.where(arr > 5, 100, arr))
arr[arr > 5] = 100
print("Replace numbers higher than 5: ", str(arr))

arr = np.arange(10)
print("Replace numbers equal to 5", np.where(arr == 5, 100, arr))
arr[arr == 5] = 100
print("Replace numbers equal to 5", str(arr))

arr = np.arange(10)
print("Replace numbers less than 5: ", np.where(arr < 5, 100, arr))
arr[arr < 5] = 100
print("Replace numbers less than 5: ", str(arr))

