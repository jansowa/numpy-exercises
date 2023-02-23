import numpy as np
from numpy import random

arr = np.arange(10)
print("Uniform distribution with replacement:")
print(random.choice(arr, size=5))

print("Uniform distribution without replacement:")
print(random.choice(arr, size=5, replace=False))


distribution = [0.15] * 5 + [0.05] * 5

print("Non-uniform distribution (higher probability of first 5 elements) with replacement:")
print(random.choice(arr, size=5, p=distribution))

print("Non-uniform distribution (higher probability of first 5 elements) without replacement:")
print(random.choice(arr, size=5, p=distribution, replace=False))
