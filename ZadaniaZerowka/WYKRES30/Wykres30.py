import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

wartosci1 = [20, 10, 30, 10, 50]
wartosci2 = [80, 60, 42, 15, 0]
nazwy = [0, 1, 2, 3, 4]
colors1 = ['rebeccapurple', 'cyan', 'olive', 'deepskyblue', 'lime']
colors2 = ['seagreen', 'darkgreen', 'khaki', 'pink']
plt.bar(nazwy, wartosci1, color=colors1)
plt.bar(nazwy, wartosci2, color=colors2, bottom=wartosci1)
plt.plot([x for x in range(0, 6)], [120 for x in range(6)], color='green')
plt.yticks([0, 20, 40, 60, 80, 100, 120, 140])
plt.ylim(0, 150)
plt.title('Tytuł')

plt.savefig('obraz30.png')
plt.show()