import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = np.arange(5)
wartosci1 = [8, -55, -60, 181, 130]
wartosci2 = [-65, 110, 181, 160, 140]
wartosci3 = [100, 190, 170, 110, 63]
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='B', color='yellowgreen')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='C', color='magenta')
plt.bar(nazwa, wartosci1, width=0.25, label='A', color='palegreen')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4])
plt.yticks([-100, -75, -24, 0, 13, 66, 90, 180])
plt.grid(axis='y')
plt.xlabel('Podpis osi x')
plt.ylabel('Podpis osi y')
plt.title('Wykres')
plt.legend()

plt.savefig('zad6.png')
plt.show()