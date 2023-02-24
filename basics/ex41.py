import numpy as np

x = np.float32(1.56)
pyx = x.item()

# y = np.float32(1.23)
y = np.int32(32)
pyy = y.item()
print(type(pyx))
print(type(pyy))
