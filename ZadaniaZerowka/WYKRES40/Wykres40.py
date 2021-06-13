import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [21, 16, 21, 21, 21]
wartosci2 = [28, 34, 25, 6, 7]
colors1 = ['forestgreen', 'olive', 'indigo', 'saddlebrown', 'magenta']
colors2 = ['blue', 'khaki', 'chartreuse', 'firebrick', 'mediumorchid']
explodes = [0.1, 0, 0, 0, 0]

plt.subplot(211)
plt.pie(wartosci1, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors1, startangle=0, explode=explodes)
plt.title('Tytuł1')
plt.subplot(212)
plt.pie(wartosci2, labels=nazwa, autopct=lambda pct: "{:.0f}%".format(pct), colors=colors2, startangle=0, explode=explodes)
plt.title('Tytuł2')


plt.savefig('obraz40.png')
plt.show()