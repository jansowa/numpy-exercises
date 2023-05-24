import numpy as np

import numpy as np
x = np.zeros((3, 4))
print("Shape", x.shape, ":")
print(x)
y = np.expand_dims(x, axis=1)
print("Expand, shape", y.shape, ":")
print(y)
z = np.expand_dims(y, axis=1)
print("Expand, Shape", z.shape, ":")
print(z)

a = np.squeeze(z, axis=1)
print("Squeeze, shape", a.shape, ":")
print(a)

b = np.squeeze(a, axis=1)
print("Squeeze, shape", b.shape, ":")
print(b)

