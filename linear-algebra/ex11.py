import numpy as np

arr = np.random.randint(0, 10, (3, 3))

print("square matrix:\n" + str(arr))
print("matrix determinant: " + str(np.linalg.det(arr)))
