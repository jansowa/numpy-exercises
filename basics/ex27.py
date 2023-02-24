import numpy as np

identity1 = np.identity(3)
print(identity1)

identity2 = np.zeros((3, 3))
identity2[0, 0] = 1
identity2[1, 1] = 1
identity2[2, 2] = 1
print(identity2)

identity3 = np.eye(3)
print(identity3)