import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [-90, -5, -60, -50, -3]
colors1 = ['blue', 'darkorange', 'lightpink', 'steelblue', 'limegreen']
plt.barh(x, wartosci1, color=colors1)
plt.title('Tytuł jhk')
wartosci2 = [23, 18, 40, 80, 10]
colors2 = ['forestgreen', 'violet', 'gold', 'tomato', 'mediumorchid']
plt.barh(x, wartosci2, color=colors2)
plt.yticks(x, nazwa)
plt.xticks([-80, -60, -40, -20, 0, 20, 40, 60, 80])
plt.xlim(-90, 90)

plt.savefig('obraz3.png')
plt.show()
