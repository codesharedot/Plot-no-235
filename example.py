import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 10*x

plt.plot(x, y,'g-.',linewidth=1)
plt.savefig('chart.png')