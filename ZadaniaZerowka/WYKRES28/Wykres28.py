import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

wartosci1 = [20, 10, 30, 10, 50]
wartosci2 = [95, 30, 100, 50, 80]
nazwy = ['A', 'B', 'C', 'D', 'E']
colors1 = ['mediumorchid', 'magenta', 'violet', 'turquoise', 'mediumaquamarine']
colors2 = ['springgreen', 'limegreen', 'orange', 'sandybrown', 'darkgreen']
plt.bar(nazwy, wartosci1, color=colors1)
plt.bar(nazwy, wartosci2, color=colors2, bottom=wartosci1)
plt.yticks([0, 20, 40, 60, 80, 100, 120, 140])
plt.ylim(0, 150)
plt.title('Tytuł')

plt.savefig('obraz28.png')
plt.show()
