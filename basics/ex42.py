import numpy as np

arr = np.array([[1, 1, 0, 2],
          [0, 3, 0, 3],
          [1, 0, 4, 4]])

sum = 0
for index, value in np.ndenumerate(arr):
    x = index[1]
    y = index[0]
    if y==0:
        sum += value
    if y>0 and arr[y-1][x] != 0:
        sum += value

print(sum)