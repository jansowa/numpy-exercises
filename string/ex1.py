import numpy as np

arr1 = np.array([['Python', 'PHP']], dtype=str)
arr2 = np.array([[' Java', ' C++']], dtype=str)

print(np.char.add(arr1, arr2))
