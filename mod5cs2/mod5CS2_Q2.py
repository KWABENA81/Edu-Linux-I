import locale

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, pylab

params = {'legend.fontsize': 'medium', 'figure.figsize': (15., 7.5),
          'axes.labelsize': 'small', 'axes.titlesize': 'small', 'figure.autolayout': True,
          'xtick.labelsize': 'small', 'ytick.labelsize': 'small'}
pylab.rcParams.update(params)

#   Read file
temp_data = pd.read_csv('777_m5_datasets_v1.0/BigMartSalesData.csv')
#   capture headers of table
df = pd.DataFrame(temp_data, columns=['Amount', 'Month', 'Year'])
df = df[df['Year'] == 2011]

df = df[['Month', 'Amount']].groupby('Month')['Amount'].sum().reset_index()

plt.xlabel('Months in 2011', fontsize=14)
plt.ylabel('Sales - x$1,000,000 dollars ', fontsize=14)
plt.grid(True)
plt.title('Total sales Per Month for 2011', fontsize=16)

y = df['Amount']
x = df['Month']

#plt.plot(x, y)
plt.grid(True)
plt.xlim(0, 13)
plt.ylim(500000., 1750000.)
plt.yticks(np.arange(500000, 1750000, 100000))
plt.xticks(np.arange(min(x) - 1, max(x) + 2, 1))

plt.bar(x, y)
plt.savefig("mod5CS2_Q2.jpg")
plt.show()
#====================================

# fig = plt.figure(figsize=(25, 85))
# plt.ylabel(y_title)
# plt.xlabel(x_title)
# plt.xticks(rotation=70)
#
# plt.title('Hurricanes in the US')
#
# plt.bar(year_data[0:101], hurricanes_data[0:101])
# plt.savefig("mod5_Q1.jpg")
# plt.show()
#
