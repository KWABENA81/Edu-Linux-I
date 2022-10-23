import locale

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, pylab

params = {'legend.fontsize': 'medium', 'figure.figsize': (15., 7.5),
          'axes.labelsize': 'small', 'axes.titlesize': 'small',
          'figure.autolayout': True, 'xtick.labelsize': 'small', 'ytick.labelsize': 'small'}
pylab.rcParams.update(params)

#   Read file
temp_data = pd.read_csv('777_m5_datasets_v1.0/BigMartSalesData.csv')
#   capture headers of table
df = pd.DataFrame(temp_data, columns=['Amount', 'Country', 'Year'])
df = df[df['Year'] == 2011]

df = df[['Country', 'Amount']].groupby('Country')['Amount'].sum()
df.plot(kind='pie', y='Sales per Country')
#
plt.savefig("mod5CS2_Q3.jpg")
plt.show()
