import numpy as np

arr = np.array([1, 2, 3, 4])
print("BEFORE CONVERTING")
print("Array: ", str(arr))
print("Array dtype: ", str(arr.dtype))

farr = arr.astype(float)
print("AFTER CONVERTING")
print("Array: ", str(farr))
print("Array dtype: ", str(farr.dtype))

farr2 = arr.asfarray(arr)
print("AFTER CONVERING IN SECOND WAY")
print("Array: ", str(farr2))
print("Array dtype: ", str(farr2.dtype))

farr3 = np.array(arr, dtype=float)
print("AFTER CONVERTING IN THIRD WAY")
print("Array: ", str(farr3))
print("Array dtype: ", str(farr3.dtype))
