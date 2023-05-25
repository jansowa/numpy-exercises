import numpy as np

arr = np.arange(1, 15)

print([arr[:2], arr[2:6], arr[6:]])
print(np.split(arr, [2, 6]))