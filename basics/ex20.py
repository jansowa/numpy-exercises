import numpy as np
from numpy import random

matrix = random.random(size=(3,4))

print("The whole matrix:")
print(matrix)
print("Iterate over the matrix:")
for x in np.nditer(matrix):
    print(x)