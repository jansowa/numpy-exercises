import numpy as np

arr = np.array([0.39536213, 0.11779404, 0.32612381, 0.16327394, 0.98837963, 0.25510787, 0.01398678, 0.15188239, 0.12057667, 0.67278699])

print(np.concatenate((np.sort(arr[:5]), arr[5:])))
print(arr[np.argpartition(arr, range(3))])
