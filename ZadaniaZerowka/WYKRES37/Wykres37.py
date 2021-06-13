import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
nazwa = [6, 10, 8, -2, 2]
wartosci1 = [-30, -10, -20, -50, -70]
wartosci2 = [30, 10, 20, 50, 70]
colors1 = ['darkred', 'darkviolet', 'purple', 'brown', 'palegreen']
colors2 = ['yellowgreen', 'darkorchid', 'darkturquoise', 'mediumturquoise', 'green']
plt.subplot(221)
plt.barh(x, wartosci1, color=colors1)
plt.yticks(x, nazwa)
plt.xlim(-70, 0)
plt.title('Tytuł1')
plt.subplot(224)
plt.barh(x, wartosci2, color=colors2)
plt.yticks(x, nazwa)
plt.xlim(0, 70)
plt.title('Tytuł2')

plt.savefig('obraz37.png')
plt.show()