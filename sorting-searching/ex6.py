import numpy as np

arr = np.array([complex(1, 2), complex(3, -1), complex(3, -2), complex(4, -3), complex(3, 5)])

order_idx = np.lexsort((arr.imag, arr.real))
print(arr.real[order_idx] + 1j * arr.imag[order_idx])
print(np.sort_complex(arr))
