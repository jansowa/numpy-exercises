import numpy as np

arr1 = np.random.randint(0, 100, (3, 3, 3))
arr2 = np.random.randint(0, 100, (3, 3, 3))

print("arr1:\n", arr1)
print("arr2:\n", arr2)

print("einsum:\n", np.einsum('mka,knb', arr1, arr2))
