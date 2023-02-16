import numpy as np

arr_w_zero = np.array([0, 1, 2, 3])
arr_wo_zero = np.array([1, 2, 3])

print(np.any(arr_w_zero))
print(np.any(arr_wo_zero))