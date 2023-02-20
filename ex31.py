import numpy as np
from numpy import random

array = random.random(size=(3, 3, 3))
print(array)

array2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(array.shape == array2.shape)
