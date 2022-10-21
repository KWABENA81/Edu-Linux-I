import dask.dataframe as dd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, pylab

params = {'legend.fontsize': 'medium', 'figure.figsize': (35, 35),
          'axes.labelsize': 'medium', 'axes.titlesize': 'large',
          'xtick.labelsize': 'small', 'ytick.labelsize': 'small'}
pylab.rcParams.update(params)

#   Read file
temp_data = pd.read_csv('777_m5_datasets_v1.0/BigMartSalesData.csv')
cols = temp_data.head(0)
# print(cols)
# print(temp_data.head(5))
#   capture headers of table
df = pd.DataFrame(temp_data, columns=['Amount', 'Month', 'Year'])
df = df[df['Year'] == 2011]
df=df[['Month','Amount']]

df= df.groupby('Month')
df.agg({'Amount':'sum'})

print('.grp_by_mth()\n', df.head())
# #   count occurrences of combined columns
# occurrences = df['Make'].value_counts().to_dict()
# print(occurrences)
#
# makes = list(occurrences.keys())
# counts = list(occurrences.values())
# plt.pie(counts, labels=makes)
# #
# plt.title('Count of Model releases by Auto Makers', fontsize=16)
# plt.savefig("mod5_Q3.jpg")
# plt.show()
