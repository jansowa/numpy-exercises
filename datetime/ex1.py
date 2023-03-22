import numpy as np

arr = np.arange("2017-03", "2017-04", np.timedelta64(1, 'D'), dtype=np.datetime64)
print(arr)