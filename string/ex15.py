import numpy as np

arr = np.array(['Python', 'PHP', 'JS', 'examples', 'html'])
print("Array:", arr)
print("Number of 'P':")
print(np.char.count(arr, 'P'))
