import numpy as np

arr = np.array([('James', 5, 48.5),
                ('Nail', 6, 52.5),
                ('Paul', 4, 42.1),
                ('Pit', 5, 40.11)],
               dtype=[('name', 'U15'), ('class', int), ('height', float)])

print(np.sort(arr, order=['class', 'height']))
