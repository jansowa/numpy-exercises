import numpy as np

arr = np.zeros((3,), dtype="i4, f8, a5")
values = [(1, 1., b'one'), (2, 2., b'two'), (3, 3., b'three')]
arr[:] = values
print(arr)

arr = np.array([(1, 1., b'one'), (2, 2., b'two'), (3, 3., b'three')], dtype="i4, f8, a5")
print(arr)