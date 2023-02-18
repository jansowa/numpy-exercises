import numpy as np

print(np.concatenate((np.zeros(10), np.ones(10), [5] * 10)))
print(np.concatenate((np.zeros(10), np.ones(10), np.ones(10) * 5)))
