import numpy as np

matrix = np.random.randint(0, 10, (3, 4))
print("matrix:\n" + str(matrix))

q, r = np.linalg.qr(matrix)
print("qr decomposition:\n")
print("q:\n" + str(q))
print("r:\n" + str(r))
