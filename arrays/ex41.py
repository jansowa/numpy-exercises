import numpy as np

samp_arr = np.arange(4, dtype=np.int64)

final_arr = np.full_like(samp_arr, 10)

print("Sample array:")
print(samp_arr)
print()

print("Final array:")
print(final_arr)