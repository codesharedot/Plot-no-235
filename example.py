import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 3*x

plt.plot(x, y,'g-.',linewidth=0)
plt.savefig('chart.png')