import numpy as np

arr1 = np.array([0, 1, 2, 3])
arr2 = np.array([[4, 5, 6, 7],
                 [8, 9, 10, 11]])


print(np.concatenate((arr1.reshape((1, 4)), arr2)))

for x, y in np.nditer([arr1, arr2]):
    print(str(x) + ":" + str(y))