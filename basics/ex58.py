import numpy as np

arr = np.random.randint(0, 10, (3, 4))
print("Array:")
print(arr)
print("Flipped array:")
print(arr[::-1, ::-1])
print("Flipped array:")
print(np.flip(arr))