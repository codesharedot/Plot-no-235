import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 3*x

plt.plot(x, y,'b-.',linewidth=8)
plt.savefig('chart.png')