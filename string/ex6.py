import numpy as np

arr = np.array(['python exercises', 'PHP', 'java', 'C++'])
print("Array: ", arr)
encoded = np.char.encode(arr, encoding='cp500')
print("Encoded: ", encoded)
decoded = np.char.decode(encoded,  encoding='cp500')
print("Decoded: ", decoded)
