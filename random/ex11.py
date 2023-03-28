import numpy as np

arr = np.random.random(15)
print("Random array:")
print(arr)
print()

arr[arr.argmax()] = -1
print("Array with maximum value replaced by -1:")
print(arr)
