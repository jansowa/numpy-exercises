import numpy as np

list = list(range(1, 9))

arr1 = np.array(list)
print(arr1)
arr1_2 = np.asarray(list)
print("Are arr1 and arr1_2 equal: ", str(np.array_equal(arr1, arr1_2)))

tuple = ((8, 4, 6), (1, 2, 3))
arr2 = np.array(tuple)
print(arr2)
arr2_2 = np.asarray(tuple)
print("Are arr2 and arr2_2 equal: ", str(np.array_equal(arr2, arr2_2)))
