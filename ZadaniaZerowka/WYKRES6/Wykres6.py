import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

wartosci1 = [20, 50, 30, 10, 60]
wartosci2 = [30, 0, 40, 80, 30]
nazwy = ['A', 'B', 'C', 'D', 'E']
kolory1 = ['yellow', 'orange', 'cyan', 'violet', 'green']
kolory2 = ['green', 'orange', 'pink', 'yellow', 'red']
plt.bar(nazwy, wartosci1, color=kolory1)
plt.bar(nazwy, wartosci2, color=kolory2, bottom=wartosci1)
plt.yticks([0, 20, 40, 60, 80, 100, 120])

plt.savefig('obraz6.png')
plt.show()
