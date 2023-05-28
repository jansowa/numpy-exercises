import numpy as np

arr = np.random.randint(0, 10, (3, 3))

print("square array:\n" + str(arr))

print("eigenvalues and right eigenvectors:\n" + str(np.linalg.eig(arr)))
