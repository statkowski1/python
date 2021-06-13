import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(0.01, 15.0, 0.01)
y1 = np.log(x)
y2 = x**2 + x

fig, ax1 = plt.subplots()
ax1.plot(x, y1, 'y')
ax1.set_xlabel('x')
ax1.set_ylabel('ln(x)', color='y')
ax1.tick_params(axis='y', labelcolor='y')

ax2 = ax1.twinx()

ax2.plot(x, y2, 'c--')
ax2.set_ylabel('x^2+x', color='c')
ax2.tick_params(axis='y', labelcolor='c')
plt.title('Dwa wykresy')

plt.savefig('obraz27.png')
plt.show()