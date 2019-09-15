import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x*x

plt.plot(x, y,'y-',linewidth=1)
plt.savefig('chart.png')