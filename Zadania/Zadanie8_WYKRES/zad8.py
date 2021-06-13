import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(-10, 10, 0.01)
y1 = x**2 + 2*x - 4
y2 = -x**3 + x - 2
y3 = np.sin(2*x + 5)

fig, ax1 = plt.subplots()
ax1.plot(x, y1, ':', color='blue', label='x^2+2x-4')
ax1.plot(x, y2, '-.', color='orange', label='-x^3+x-2')
ax1.set_xlabel('oś pozioma')
ax1.set_ylabel('oś pionowa po lewej stronie')
ax1.tick_params(axis='y')
plt.ylim(-1200, 1200)
plt.xlim(-15, 15)
plt.legend(loc='upper right')

ax2 = ax1.twinx()

ax2.plot(x, y3, '--', color='green', label='sin(2x+5)')
ax2.set_ylabel('oś pionowa po prawej stronie')
ax2.tick_params(axis='y')
plt.title('Parę wykresów')
plt.ylim(-2, 2)
plt.grid(axis='y')
plt.tight_layout()
plt.legend(loc='lower right')

plt.savefig('zad8.png')
plt.show()