import numpy as np

arr = np.random.randint(0, 10, (2, 3))
print("array:\n" + str(arr))
print("condition number: " + str(np.linalg.cond(arr)))
