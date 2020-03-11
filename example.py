import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 6*x

plt.plot(x, y,'g-.',linewidth=8)
plt.savefig('chart.png')