import numpy as np

print(np.atleast_1d(12.0))
print(np.atleast_1d(12.0, 13.0, 11))
print(np.atleast_1d([12, 13]))
print(np.atleast_1d([1, 2], [3, 4]))
print(np.atleast_1d([[1, 2], [3, 4]]))