import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 10, 0.1)
y = np.cos(x)
print(y)
plt.plot(x, y, label='test')
plt.legend()
# plt.show()
plt.savefig("1.png")