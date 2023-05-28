import numpy as np

arr1 = np.random.randint(0, 10, (2, 3))
print("array 1:\n" + str(arr1))

arr2 = np.random.randint(0, 10, (2, 3))
print("array 2:\n" + str(arr2))
print("Kronecker product of arrays:\n" + str(np.kron(arr1, arr2)))
