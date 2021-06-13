import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x1 = np.arange(5)
nazwa1 = [6, 10, 8, -2, 2]
wartosci1 = [-30, -10, -20, -50, -70]
colors1 = ['deeppink', 'crimson', 'steelblue', 'lime', 'orchid']
plt.subplot(221)
plt.barh(x1, wartosci1, color=colors1)
plt.yticks(x1, nazwa1)
plt.xlim(-70, 0)
plt.title('Tytuł1')

x2 = np.arange(5)
nazwa2 = [6, 10, 8, -2, 2]
wartosci2 = [30, 10, 20, 50, 70]
colors2 = ['darkturquoise', 'palevioletred', 'dodgerblue', 'yellowgreen', 'slateblue']
plt.subplot(224)
plt.barh(x2, wartosci2, color=colors2)
plt.yticks(x2, nazwa2)
plt.xlim(0, 70)
plt.title('Tytuł2')

plt.savefig('obraz2.png')
plt.show()