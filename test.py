import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#  print(plt.style.available)
plt.style.use('ggplot')
#  plt.options.display.mpl_style = 'default'
#  MVL040517.csv

mvl = pd.read_csv('~/Downloads/MVL040517.csv')

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
