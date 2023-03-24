import numpy as np

arr = np.random.randint(-100, 100, (5, 5))
print("Array:")
print(arr)
print()

number = np.random.randint(-100, 100)
print("Number:")
print(number)
print()

argmin = np.argmin(np.abs(arr - number))
closest_value = arr.reshape((-1,))[argmin]
print("Value from array closest to number", ": ", closest_value)
closest_value2 = arr.flat[np.abs(arr - number).argmin()]
print("Value from array closest to number", ": ", closest_value2)
# print(closest_value)
# print(arr[argmin])