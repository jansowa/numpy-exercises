import numpy as np
from numpy import random
rows_number = int(input("Enter rows number: "))
columns_number = int(input("Enter columns number: "))

arr = random.random(size=(rows_number, columns_number))
print(arr)

arr2 = np.arange(1, rows_number*columns_number+1).reshape((rows_number, columns_number))
arr3 = np.arange(1, rows_number*columns_number+1).reshape((rows_number, -1))
arr4 = np.arange(1, rows_number*columns_number+1).reshape((-1, columns_number))

print(arr2)
print("Are arr2 and arr3 equal: ", str(np.array_equal(arr2, arr3)))
print("Are arr2 and arr4 equal: ", str(np.array_equal(arr2, arr4)))
