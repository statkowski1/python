import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

wartosci1 = [20, 10, 30, 12, 45]
wartosci2 = [10, 40, 40, 8, 20]
nazwy = ['A', 'B', 'C', 'D', 'E']
colors1 = ['skyblue', 'mediumspringgreen', 'lightseagreen', 'darkturquoise', 'dodgerblue']
colors2 = ['lime', 'khaki', 'cyan', 'orange', 'yellowgreen']
plt.bar(nazwy, wartosci1, color=colors1)
plt.bar(nazwy, wartosci2, color=colors2, bottom=wartosci1)
plt.yticks([0, 20, 40, 60, 80, 100, 120, 140])
plt.ylim(0, 150)
plt.title('Tytuł')

plt.savefig('obraz29.png')
plt.show()
