import typing

import numpy as np
from numpy.typing import ArrayLike

def equalwithtolerance(x: ArrayLike, y:ArrayLike, tolerance: typing.Union[int, float]) -> ArrayLike:
    return np.all(np.abs(x - y) < tolerance)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])

print(equalwithtolerance(x, y, 5))
print(equalwithtolerance(a, b, 2))

def equalwithtolerance2(x: ArrayLike, y:ArrayLike, rtol: typing.Union[int, float], atol: typing.Union[int, float]) -> ArrayLike:
    return np.allclose(x, y, rtol=rtol, atol=atol)

print(equalwithtolerance2(x, y, 5, 5))
print(equalwithtolerance2(a, b, 2, 2))