import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [27, 3, 22, 25, 23]
wartosci2 = [0, 30, 21, 4, 45]
wartosci3 = [23, 23, 16, 21, 17]
wartosci4 = [25, 15, 22, 13, 24]
colors1 = ['limegreen', 'darkgoldenrod', 'forestgreen', 'magenta', 'orchid']
colors2 = ['white', 'tomato', 'darkturquoise', 'orchid', 'limegreen']
colors3 = ['mediumblue', 'darkkhaki', 'peru', 'seagreen', 'darkorchid']
colors4 = ['lightgray', 'steelblue', 'bisque', 'navy', 'mediumseagreen']
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

plt.savefig('obraz35.png')
plt.show()