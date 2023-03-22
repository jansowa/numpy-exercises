from datetime import datetime, timedelta

import numpy as np

arr = np.arange("2000-01-01", "2000-01-02", np.timedelta64(1, 'h'), dtype=np.datetime64).astype(datetime)
print(arr)

date = datetime(2000, 1, 1)
print(np.array([date + timedelta(hours=delta) for delta in range(24)]))