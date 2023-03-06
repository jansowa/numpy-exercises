import numpy as np

arr = np.array(['python exercises', 'PHP', 'java', 'C++'])
print("Array: ", arr)
print()

print("Left: ", np.char.ljust(arr, 15, fillchar="_"))
print()

print("Right: ", np.char.rjust(arr, 15, fillchar="_"))
print()

print("Center: ", np.char.center(arr, 15, fillchar="_"))
