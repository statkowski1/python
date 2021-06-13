import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

wartosci1 = [20, 10, 30, 10, 50]
wartosci2 = [70, 60, 90, 95, 70]
nazwy = ['A', 'B', 'C', 'D', 'E']
kolory1 = ['lime', 'cyan', 'lightskyblue', 'darkkhaki', 'mediumblue']
kolory2 = ['mediumturquoise', 'steelblue', 'cadetblue', 'gold', 'crimson']
plt.bar(nazwy, wartosci1, color=kolory1)
plt.bar(nazwy, wartosci2, color=kolory2, bottom=wartosci1)
plt.yticks([0, 20, 40, 60, 80, 100, 120, 140])
plt.title('Tytuł')

plt.savefig('obraz7.png')
plt.show()