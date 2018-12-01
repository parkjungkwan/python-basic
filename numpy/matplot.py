import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)

plt.title("사인 웨이브 폼")

plt.plot(x, y)
plt.show()