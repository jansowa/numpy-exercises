import numpy as np

arr = np.array(['Python', 'PHP', 'JS', 'EXAMPLES', 'HTML'])

print("Array: ", arr)
print("Index of first 'P' occurrence:")
print(np.char.find(arr, 'P'))
