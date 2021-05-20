import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = np.arange(5)
wartosci1 = [78, 82, 66, 67, 35]
wartosci2 = [19, 24, 85, 35, 85]
wartosci3 = [62, 95, 64, 72, 25]
plt.bar(nazwa, wartosci1, width=0.25, label='B', color='#B7633D')
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='C', color='#142B70')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='A', color='#99A543')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4])
plt.title('Wykres')
plt.xlabel('Podpis osi x')
plt.ylabel('Podpis osi y')
plt.legend(loc='upper left')
plt.grid(axis='y')
plt.savefig('obraz.png')
plt.show()