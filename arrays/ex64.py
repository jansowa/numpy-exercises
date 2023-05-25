import numpy as np

print(np.repeat(np.arange(5).reshape(1, 5), 5, axis=0))

print(np.zeros((5, 5)) + np.arange(5))