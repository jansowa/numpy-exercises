import numpy as np

arr = np.array(["  both    ", "     left", "right     "])
print("Array: ", arr)

print("Removed trailing whitespaces: ", np.char.rstrip(arr))
