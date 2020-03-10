import numpy as np
import matplotlib.pyplot as plt

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
m_means = [1,1,7,4,6]
m_std = [2, 3, 4, 1, 2]
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

ax.bar(labels, m_means, width, yerr=m_std, label='Data')
ax.set_ylabel('Scores')
ax.set_title('Visual')
ax.legend()
#plt.show()
plt.savefig('chart.png')