import numpy as np

print("Arrays with at least two dimensions:")
input = 1
print("Input", input)
print("Output with at keast two dimensions", np.atleast_2d(input))
print("Output with at least three dimensions", np.atleast_3d(input))

print()
input = [1, 2]
print("Input", input)
print("Output with at keast two dimensions", np.atleast_2d(input))
print("Output with at least three dimensions", np.atleast_3d(input))

print()
input = [[1, 2], [3, 4]]
print("Input", input)
print("Output with at keast two dimensions", np.atleast_2d(input))
print("Output with at least three dimensions", np.atleast_3d(input))

print()
input = [[[1, 2], [3, 4]],
         [[5, 6], [7, 8]]]
print("Input", input)
print("Output with at keast two dimensions", np.atleast_2d(input))
print("Output with at least three dimensions", np.atleast_3d(input))
