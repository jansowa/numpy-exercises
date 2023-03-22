import numpy as np
import datetime

now = np.datetime64('now')
print(now)
ts = np.float64(now)
print(ts)
print(datetime.datetime.utcfromtimestamp(ts))
