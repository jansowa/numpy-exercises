import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("Sum of all elements:")
print(np.sum(array))

print("Sums of consecutive columns:")
print(np.sum(array, axis=0))

print("Sums of consecutive columns:")
for col_idx in range(array.shape[1]):
    print(np.sum(array[:, col_idx]))

print("Sums of consecutive columns:")
for col in array.T:
    print(np.sum(col))

print("Sums of consecutive columns:")
print([np.sum(col) for col in array.T])

print("Sums of consecutive rows:")
print(np.sum(array, axis=1))

print("Sums of consecutive rows:")
for row_idx in range(array.shape[0]):
    print(np.sum(array[row_idx, :]))

print("Sums of consecutive rows:")
for row in array:
    print(np.sum(row))

print("Sums of consecutive rows:")
print([np.sum(row) for row in array])