import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
nazwa = [6, 10, 8, -2, 2]
wartosci = [-30, -10, -20, -50, -70]
colors1 = ['maroon', 'darkgoldenrod', 'blueviolet', 'lime', 'violet']
plt.subplot(211)
plt.barh(x, wartosci, color=colors1)
plt.yticks(x, nazwa)
plt.xlim(-70, 0)
plt.title('Tytuł1')

wartosci1 = [25, 10, 30, 10, 50]
wartosci2 = [25, 45, 25, 40, 25]
nazwy = ['A', 'B', 'C', 'D', 'E']
colors1 = ['orange', 'deepskyblue', 'powderblue', 'darkblue', 'aqua']
colors2 = ['magenta', 'mediumturquoise', 'cornflowerblue', 'darkorchid', 'maroon']
plt.subplot(212)
plt.bar(nazwy, wartosci1, color=colors1)
plt.bar(nazwy, wartosci2, color=colors2, bottom=wartosci1)
plt.yticks([0, 25, 50, 75, 100, 125, 150])
plt.title('Tytuł')
plt.tight_layout()

plt.savefig('obraz25.png')
plt.show()