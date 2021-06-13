import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
nazwa = ['A', 'B', 'C', 'D', 'E']
wartosci1 = [-40, -80, -40, -90, -60]
colors1 = ['royalblue', 'firebrick', 'mediumvioletred', 'saddlebrown', 'mediumaquamarine']
plt.barh(x, wartosci1, color=colors1)
plt.title('Tytuł jhk')
wartosci2 = [60, 10, 5, 55, 70]
colors2 = ['indigo', 'gold', 'indianred', 'skyblue', 'mediumblue']
plt.barh(x, wartosci2, color=colors2)
plt.yticks(x, nazwa)
plt.xticks([-80, -60, -40, -20, 0, 20, 40, 60, 80])
plt.xlim(-90, 90)

plt.savefig('obraz4.png')
plt.show()
