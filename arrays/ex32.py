import numpy as np

arr = np.random.random(size=(3, 4))

print("Array:")
print(arr)
print()

path = 'ex32.txt'
np.savetxt(path, arr)

loaded_arr = np.loadtxt(path)
print("Loaded array:")
print(loaded_arr)