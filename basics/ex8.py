import numpy as np

print(np.iscomplex(0))
print(np.iscomplex(np.inf))
print(np.iscomplex(complex(1, 1)))
print(np.iscomplex(complex(np.inf, -np.inf)))

print(np.isreal(0))
print(np.isreal(np.inf))
print(np.isreal(complex(1, 1)))
print(np.isreal(complex(np.inf, -np.inf)))

print(np.isreal([0, 1]))

print(np.isscalar(1))
print(np.isscalar([0, 1]))
print(np.isscalar(False))
print(np.isscalar(complex(1, 2)))
print(np.isscalar(np.inf))