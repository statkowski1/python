import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [3299, 2823, 1122, 2415, 340]
wartosci2 = [2019, 282, 939, 3991, 2770]
wartosci3 = [581, 2713, 2403, 2868, 1434]
wartosci4 = [3177, 1927, 1302, 417, 3177]
colors1 = ['hotpink', 'mediumpurple', 'darkorchid', 'saddlebrown', 'fuchsia']
colors2 = ['darkmagenta', 'lime', 'sienna', 'burlywood', 'cornflowerblue']
colors3 = ['mediumseagreen', 'chocolate', 'springgreen', 'deepskyblue', 'forestgreen']
colors4 = ['mediumslateblue', 'palegreen', 'darkcyan', 'tan', 'greenyellow']
plt.subplot(221)
plt.pie(wartosci1, labels=nazwa, autopct=lambda pct: "{:.2f}".format(pct), colors=colors1, startangle=0)
plt.title('Tytuł1')
plt.subplot(222)
plt.pie(wartosci2, labels=nazwa, autopct=lambda pct: "{:.2f}".format(pct), colors=colors2, startangle=0)
plt.title('Tytuł2')
plt.subplot(223)
plt.pie(wartosci3, labels=nazwa, autopct=lambda pct: "{:.2f}".format(pct), colors=colors3, startangle=0)
plt.title('Tytuł3')
plt.subplot(224)
plt.pie(wartosci4, labels=nazwa, autopct=lambda pct: "{:.2f}".format(pct), colors=colors4, startangle=0)
plt.title('Tytuł4')

plt.savefig('obraz34.png')
plt.show()