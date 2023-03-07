import numpy as np

arr1 = np.array(['Hello', 'PHP', 'JS', 'examples', 'html'])
arr2 = np.array(['Hello', 'php', 'Java', 'examples', 'html'])

print("Equal test:")
print(np.char.equal(arr1, arr2))
print("Not equal test:")
print(np.char.not_equal(arr1, arr2))
print("Less equal test:")
print(np.char.less_equal(arr1, arr2))
print("Greater equal test:")
print(np.char.greater_equal(arr1, arr2))
print("Less test:")
print(np.char.less(arr1, arr2))
