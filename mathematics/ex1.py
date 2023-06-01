import numpy as np

arr1 = np.random.randint(0, 10, (3, 4))
arr2 = np.random.randint(0, 10, (3, 4))

print("array 1:\n" + str(arr1))
print("array 2:\n" + str(arr2))
print("Add elements element-wise:\n" + str(arr1+arr2))
print("Subtract elements element-wise:\n" + str(arr1-arr2))
print("Multiply elements element-wise:\n" + str(arr1*arr2))
print("Divide elements element-wise:\n" + str(arr1/arr2))
