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
colors1 = ['blueviolet', 'magenta', 'limegreen', 'forestgreen', 'darkslateblue']
plt.subplot(221)
plt.barh(x, wartosci, color=colors1)
plt.yticks(x, nazwa)
plt.xlim(-70, 0)
plt.title('Tytuł1')

x1 = [-2, -1, 0, 1, 2, 3]
y1 = [-2, -1, 0, 1, 2, 3]
x2 = [-2, -1, 0, 1, 2, 3]
y2 = [5, 4, 3, 2, 1, 0]
plt.subplot(224)
plt.plot(x1, y1, 'r^', label='opcja 1')
plt.plot(x2, y2, 'bs', label='opcja 2')
plt.xticks([-2, -1, 0, 1, 2, 3])
plt.legend(loc='center right')
plt.title('tytuł')

plt.savefig('obraz23.png')
plt.show()