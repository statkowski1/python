import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = np.arange(5)
wartosci1 = [10, 85, 82, 38, 50]
wartosci2 = [60, 42, 72, 93, 75]
wartosci3 = [83, 95, 67, 30, 42]
plt.bar(nazwa, wartosci1, width=0.25, label='B', color='#6DCCA1')
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='C', color='#D39F6C')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='A', color='#0F99AC')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4])
plt.grid(axis='y')
plt.title('Wykres')
plt.legend()
plt.show()
