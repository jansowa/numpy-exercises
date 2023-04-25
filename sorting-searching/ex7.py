import numpy as np

n = 4
arr = np.array([70, 50, 20, 30, -11, 60, 50, 40])

element = arr[n-1]

print(np.concatenate((arr[arr <= element], arr[arr > element])))
print(np.partition(arr, n))