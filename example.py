import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 7*x*x

plt.plot(x, y,'m-',linewidth=4)
plt.savefig('chart.png')