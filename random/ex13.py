import numpy as np

arr = np.random.randint(0, 10, 20)
freq = dict()
for i in range(10):
    freq[i] = 0

for number in arr:
    freq[number] += 1
argmax = np.argmax(freq.values())
print("Array:")
print(arr)
print()

print("Frequencies of numbers in array:")
print(freq)
print()

print("Value with highest frequency:")
print(np.bincount(arr).argmax())

print("Value with highest frequency:")
print(np.argmax(list(freq.values())))
