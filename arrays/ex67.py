import numpy as np

arr = np.random.random(10)
arr.setflags(write=False)

# Returns ValueError, because arr is immutable
arr[1] = 5