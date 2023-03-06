import numpy as np

arr = np.array(["  both    ", "     left", "right     "])
print("Array: ", arr)
print("Stripped: ", np.char.strip(arr))
