import numpy as np

arr = np.array(['PHP Exercises, Practice, Solution'])

print("Original array:")
print(arr)
print()

print("Array with \"PHP\" replaced by \"Python\":")
print(np.char.replace(arr, "PHP", "Python"))
