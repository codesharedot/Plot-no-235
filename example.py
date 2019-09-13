import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 4*x

plt.plot(x, y,'y:',linewidth=10)
plt.savefig('chart.png')