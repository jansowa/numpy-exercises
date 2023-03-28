import numpy as np

array = np.random.randint(0, 99, 100)
value = np.random.uniform(0, 99)
print(array)
print(value)

print(array[np.argmin(np.abs(array - value))])