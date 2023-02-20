import numpy as np

list = [1, 2, 3, 4]
nparr = np.array(list)
list2 = nparr.tolist()
print("First list:")
print(list)
print("Second list:")
print(list2)
print("Are lists equal: ", str(list == list2))