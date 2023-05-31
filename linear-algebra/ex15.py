import numpy as np

matrix = np.random.randint(0, 10, (3, 4))

print("matrix:\n" + str(matrix))

print("sum of diagonal elements: " + str(np.diag(matrix).sum()))
print("sum of diagonal elements: " + str(np.trace(matrix)))
