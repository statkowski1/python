import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x1 = [-2, -1, 0, 1, 2, 3]
y1 = [9, -1, 0, 0, 8, 1]
x2 = [-2, -1, 0, 1, 2, 3]
y2 = [-1, 6, 2, 5, -1, 0]


plt.plot(x1, y1, 'r^', label='opcja 1')
plt.plot(x2, y2, 'bs', label='opcja 2')
plt.title('tytuł')
plt.legend(loc='upper right')

plt.savefig('obraz36.png')
plt.show()