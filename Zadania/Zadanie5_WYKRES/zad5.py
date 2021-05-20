import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

nazwa = np.arange(5)
wartosci1 = [75, -75, 50, -40, 110]
wartosci2 = [175, 52, -10, -20, 110]
wartosci3 = [70, -70, 35, 180, 0]
plt.bar(nazwa, wartosci1, width=0.25, label='B', color='#8A8567')
plt.bar(nazwa+0.25, wartosci2, width=0.25, label='C', color='#5C7C57')
plt.bar(nazwa+0.5, wartosci3, width=0.25, label='A', color='#DCA19D')
plt.xticks([0.25, 1.25, 2.25, 3.25, 4.25], [0, 1, 2, 3, 4])
plt.title('Wykres')
plt.xlabel('Podpis osi x')
plt.ylabel('Podpis osi y')
plt.legend()
plt.grid()
plt.savefig('obraz.png')
plt.show()