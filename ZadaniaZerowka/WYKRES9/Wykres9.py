import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
import seaborn as sns

plt.plot([0, 1, 2, 3, 4, 5, 6, 7], [2, 1, -2, -3, 2, -3, 2, -2], label='33')
plt.plot([-2, -1, 0, 1, 3, 5], [3, -3, 3, 1, 3, 1], label='333')
plt.text(2.5, 0.5, 'ABCD')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Tytuł1')
plt.legend(loc='center left')
plt.grid()

plt.savefig('obraz9.png')
plt.show()
