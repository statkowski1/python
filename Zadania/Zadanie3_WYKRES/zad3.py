import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = np.arange(5)
wartosci1 = [23, 77, 138, 80, 75]
wartosci2 = [124, 119, 20, 92, 138]
wartosci3 = [23, 48, 77, 110, 57]
plt.bar(nazwa, wartosci1, width=0.25, label='B', color='#AFAC9E')
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='C', color='#BBC38F')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='A', color='#A25D75')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4])
plt.grid()

plt.show()