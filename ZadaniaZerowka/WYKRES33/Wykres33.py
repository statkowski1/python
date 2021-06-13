import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [2470, 1677, 2195, 2348, 1311]
wartosci2 = [1954, 1437, 3103, 920, 2586]
wartosci3 = [1615, 3043, 2547, 994, 1801]
wartosci4 = [637, 1497, 2611, 2452, 2803]
colors1 = ['darkred', 'yellowgreen', 'cornflowerblue', 'limegreen', 'goldenrod']
colors2 = ['mediumaquamarine', 'lime', 'deeppink', 'darkgoldenrod', 'lightsteelblue']
colors3 = ['limegreen', 'seagreen', 'mediumvioletred', 'darkorchid', 'mediumseagreen']
colors4 = ['teal', 'magenta', 'rosybrown', 'mediumspringgreen', 'dimgray']
plt.subplot(221)
plt.pie(wartosci1, labels=nazwa, autopct=lambda pct: "{:.2f}%".format(pct), colors=colors1, startangle=0)
plt.title('Tytuł1')
plt.subplot(222)
plt.pie(wartosci2, labels=nazwa, autopct=lambda pct: "{:.2f}%".format(pct), colors=colors2, startangle=0)
plt.title('Tytuł2')
plt.subplot(223)
plt.pie(wartosci3, labels=nazwa, autopct=lambda pct: "{:.2f}%".format(pct), colors=colors3, startangle=0)
plt.title('Tytuł3')
plt.subplot(224)
plt.pie(wartosci4, labels=nazwa, autopct=lambda pct: "{:.2f}%".format(pct), colors=colors4, startangle=0)
plt.title('Tytuł4')

plt.savefig('obraz33.png')
plt.show()