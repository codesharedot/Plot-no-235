import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 10*x*x

plt.plot(x, y,'r:',linewidth=8)
plt.savefig('chart.png')