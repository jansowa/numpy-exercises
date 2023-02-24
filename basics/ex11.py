import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])

print(np.equal(x, y))
print(np.equal(a, b))

print(np.isclose(x, y, atol=1, rtol=1))
print(np.isclose(a, b, atol=1, rtol=1))
