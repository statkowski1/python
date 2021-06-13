import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

x = np.arange(5)
wartosci1 = [-30, -10, -20, -50, -70]
wartosci2 = [30, 10, 20, 50, 70]
nazwy = ['6', '10', '8', '-2', '2']
colors1 = ['hotpink', 'black', 'limegreen', 'lime', 'greenyellow']
colors2 = ['indigo', 'violet', 'crimson', 'saddlebrown', 'mediumvioletred']
plt.subplot(321)
plt.barh(x, wartosci1, color=colors1)
plt.title('Tytuł1')
plt.xlim(-70, 0)
plt.yticks(x, nazwy)
plt.subplot(326)
plt.barh(x, wartosci2, color=colors2)
plt.title("Tytuł2")
plt.xlim(0, 70)
plt.yticks(x, nazwy)
plt.tight_layout()
plt.savefig('obraz1.png')
plt.show()
