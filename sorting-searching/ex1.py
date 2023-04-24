import numpy as np

arr = np.array([[10, 40],
                [30, 20]])

print("Original array:")
print(arr)
print()

print("Sort along the first axis:")
arr.sort(axis=0)
print(arr)
print()

arr = np.array([[10, 40],
                [30, 20]])
print("Sort along the last axis:")
arr.sort(axis=-1)
print(arr)

arr = np.array([[10, 40],
                [30, 20]])
print("Sort flattened array:")
arr = np.array(arr.flat)
arr.sort()
print(arr)



arr = np.array([[10, 40],
                [30, 20]])

print("Original array:")
print(arr)
print()

print("Sort along the first axis:")
print(np.sort(arr, axis=0))
print()

print("Sort along the last axis:")
print(np.sort(arr))

print("Sort flattened array:")
print(np.sort(arr, axis=None))