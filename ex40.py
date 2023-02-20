import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.0000001)
y = np.sin(x)

print(len(x))
plt.plot(x, y)
plt.show()
