import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

slownik = {'A': 21, 'B': 27, 'C': 33, 'D': 15, 'E': 35}
colors = [ '#d82647' ,'#2af6ea','#af768a' ,'#a2d1ef', '#7c1b53']
plt.figure(figsize=(6, 6))
plt.pie(slownik.values(), labels=slownik.values(), colors=colors, startangle = 90)
plt.title('Tytuł')
plt.legend(slownik.keys(), loc='upper left')
plt.savefig('obraz.png')
plt.show()