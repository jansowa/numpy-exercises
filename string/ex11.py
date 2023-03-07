import numpy as np

arr = np.array(['First\nsecond\nthird'])

print("Array:", arr)
print("Splitted by newlines: ", np.char.splitlines(arr))
