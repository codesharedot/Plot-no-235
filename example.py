import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 6*x

plt.plot(x, y,'b:',linewidth=1)
plt.savefig('chart.png')