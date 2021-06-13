import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [23, 13, 30, 3, 30]
wartosci2 = [10, 19, 21, 24, 26]
wartosci3 = [39, 1, 44, 2, 13]
wartosci4 = [13, 4, 33, 6, 44]
colors1 = ['bisque', 'greenyellow', 'lightsteelblue', 'palevioletred', 'peru']
colors2 = ['cornflowerblue', 'blueviolet', 'mediumorchid', 'yellowgreen', 'royalblue']
colors3 = ['darkorchid', 'green', 'hotpink', 'fuchsia', 'blueviolet']
colors4 = ['aqua', 'bisque', 'slateblue', 'wheat', 'greenyellow']
plt.subplot(221)
plt.pie(wartosci1, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors1, startangle=0)
plt.title('Tytuł1')
plt.subplot(222)
plt.pie(wartosci2, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors2, startangle=0)
plt.title('Tytuł2')
plt.subplot(223)
plt.pie(wartosci3, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors3, startangle=0)
plt.title('Tytuł3')
plt.subplot(224)
plt.pie(wartosci4, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors4, startangle=0)
plt.title('Tytuł4')

plt.savefig('obraz39.png')
plt.show()