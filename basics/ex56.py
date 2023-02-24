import numpy as np

arr = np.array([[[1, 2, 1, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [1, 2, 1, 0]],

                [[1, 2, 1, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [1, 2, 1, 0]],

                 [[1, 2, 1, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [2, 1, 3, 0],
                 [1, 2, 1, 0]]
                ])

print("Array shape:")
print(arr.shape)
print("Array:")
print(arr)

print("Random array:")
print(np.random.randint(0, 10, (3, 5, 4)))