import numpy as np

vector = np.arange(21)
print(list(map(lambda x: -x if 9 <= x and x <= 15 else x, vector)))

x = np.arange(21)
x[(x >= 9) & (x <= 15)] *= -1
print(x)