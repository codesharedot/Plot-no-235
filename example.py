import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 7*x

plt.plot(x, y,'y-.',linewidth=6)
plt.savefig('chart.png')