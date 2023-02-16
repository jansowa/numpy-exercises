import numpy as np

arr_w_zero = np.array([0, 1, 2, 3])
arr_wo_zero = np.array([1, 2, 3])

print(0 not in arr_w_zero)
print(0 not in arr_wo_zero)

print(np.all(arr_w_zero))
print(np.all(arr_wo_zero))