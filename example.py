import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 1*x

plt.plot(x, y,'b-.',linewidth=9)
plt.savefig('chart.png')