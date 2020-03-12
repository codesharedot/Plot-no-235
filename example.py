import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 4*x

plt.plot(x, y,'r-.',linewidth=4)
plt.savefig('chart.png')