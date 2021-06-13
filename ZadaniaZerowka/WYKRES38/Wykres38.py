import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(0.01, 15.0, 0.01)
y1 = -x**2 - 4*x - 4
y2 = x**2 + x + 99

fig, ax1 = plt.subplots()
ax1.plot(x, y1, 'g')
ax1.set_xlabel('x')
ax1.set_ylabel('-x^2-4x-4', color='green')
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()

ax2.plot(x, y2, 'b--')
ax2.set_ylabel('x^2+x+99', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')
plt.title('Dwa wykresy')

plt.savefig('obraz38.png')
plt.show()