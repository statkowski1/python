import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = [0, 1, 2, 3, 4, 5]
wartosci1 = [-48, -12, -20, -50, -25, -30]
wartosci2 = [45, 20, 28, 30, 38, 37]
wartosci3 = [42, 20, 28, 30, 28, 37]

plt.barh(x, wartosci2, color='purple', label='A')
plt.barh(x, wartosci1, color='blue', label='B')
plt.barh(x, wartosci3, color='magenta', left=wartosci2, label='C')
plt.xlim(-60, 98)
plt.xticks([-48, 1, 32, 82, 98])
plt.grid(axis='x')
plt.title('Tytuł wykresu')
plt.legend(loc='upper right')

plt.savefig('zad7.png')
plt.show()