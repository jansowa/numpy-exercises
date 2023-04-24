import numpy as np

arr = np.array([('James', 324, 48.5),
                ('Nail', 234, 52.5),
                ('Paul', 423, 42.1),
                ('Pit', 519, 40.11)],
               dtype=[('name', 'U15'), ('id', int), ('height', float)])
sorted_idx = np.argsort(arr, order='height')
print(sorted_idx)
print(arr[sorted_idx])

ids = [324, 234, 423, 519]
heights = [48.5, 52.5, 42.1, 40.11]

sorted_idx = np.lexsort((ids, heights))
print(sorted_idx)
print(np.array([ids, heights]).T[sorted_idx])