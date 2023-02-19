import numpy as np

array = np.random.randint(0, 100, size=(3, 4))
print("Array:")
print(array)

print()
print("Number of rows: " + str(array.shape[0]))
print("Number of columns: " + str(array.shape[1]))
