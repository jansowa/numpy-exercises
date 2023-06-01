import numpy as np

arr = np.random.randint(0, 10, 2)
print("array: " + str(arr))

print("log of sum of exponentations: " + str(np.log(np.exp(arr).sum())))
print("log of sum of exponentations: " + str(np.logaddexp(arr[0], arr[1])))
print("log2 of sum of exponentations: " + str(np.log2(np.power(2, arr).sum())))
print("log2 of sum of exponentations: " + str(np.logaddexp2(arr[0], arr[1])))
