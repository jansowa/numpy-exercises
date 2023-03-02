import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(a > b)
print(np.greater(a, b))
print(a >= b)
print(np.greater_equal(a, b))
print(a < b)
print(np.less(a, b))
print(a <= b)
print(np.less_equal(a, b))
