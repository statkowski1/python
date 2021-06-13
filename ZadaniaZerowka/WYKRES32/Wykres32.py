import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
nazwa = [11, 12, 13, 14, 15]
wartosci1 = [-70, -68, -35, -5, -90]
wartosci2 = [85, 70, 90, 40, 90]
colors1 = ['skyblue', 'orangered', 'wheat', 'lightskyblue', 'mediumblue']
colors2 = ['silver', 'hotpink', 'saddlebrown', 'darkviolet', 'deepskyblue']
plt.barh(x, wartosci1, color=colors1)
plt.barh(x, wartosci2, color=colors2)
plt.yticks(x, nazwa)
plt.xticks([-80, -60, -40, -20, 0, 20, 40, 60, 80])
plt.xlim(-90, 90)
plt.title('Tytuł jhk')

plt.savefig('obraz32.png')
plt.show()