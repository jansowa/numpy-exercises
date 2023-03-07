import numpy as np

arr = np.array(['2', '11', '234', '1234', '12345'])
print("Original array:")
print(arr)
print()

print("Array with zeros filled from the left side (size 5 chars):")
print(np.char.rjust(arr, 5, fillchar='0'))
