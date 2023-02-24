import numpy as np

arr = np.array([[1, np.nan, np.inf],
               [np.nan, 45, np.nan],
               [123, 32, np.nan]])

print(np.isnan(arr))