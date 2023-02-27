import numpy as np

fahr = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Values in Fahrenheit degrees:")
print(fahr)

print("Values in Celsius degrees:")
print(np.round((fahr - 32) * 5 / 9, 2))

cels = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print("Values in Celsius degrees:")
print(cels)

print("Values in Fahrenheit degrees:")
print(np.round(32 + cels * 9 / 5), 2)