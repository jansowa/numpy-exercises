import numpy as np

arr = np.random.randint(0, 10, (3, 3))

print("matrix:\n" + str(arr))

print("matrix inverse:\n" + str(np.linalg.inv(arr)))