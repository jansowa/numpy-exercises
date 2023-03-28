import numpy as np

arr = np.random.random((10, 2))

r = np.sqrt(np.square(arr[:, 0]) + np.square(arr[:, 1]))

theta = np.arctan(arr[:, 1] / arr[:, 0])
theta2 = np.arctan2(arr[:, 1], arr[:, 0])

print(np.array([r, theta]).reshape((10, 2)))
print(np.array([r, theta2]).reshape((10, 2)))