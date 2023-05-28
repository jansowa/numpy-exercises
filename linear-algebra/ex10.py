import numpy as np

matrix = np.random.randint(0, 10, (3, 4))
print("matrix:\n" + str(matrix))
print("matrix norm: " + str(np.linalg.norm(matrix)))

vector = np.random.randint(0, 10, 5)
print("vector: " + str(vector))
print("vector norm: " + str(np.linalg.norm(vector)))
