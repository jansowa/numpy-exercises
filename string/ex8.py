import numpy as np

arr = np.array(["  both    ", "     left", "right     "])
print("Array: ", arr)

print("Removed leading whitespaces: ", np.char.lstrip(arr))
