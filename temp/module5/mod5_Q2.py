import dask.dataframe as dd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, pylab

#   Read file
temp_data = pd.read_csv('inputs/CityTemps.csv')
params = {'legend.fontsize': 'medium', 'figure.figsize': (15, 5),
          'axes.labelsize': 'medium', 'axes.titlesize': 'x-large',
          'xtick.labelsize': 'small', 'ytick.labelsize': 'small'}
pylab.rcParams.update(params)

#   capture dataframe
df = pd.DataFrame(temp_data, columns=['Year', 'Month', 'Moscow', 'San Francisco'])
# extract the axis data
df['list'] = df[['Year', 'Month']].values.tolist()
df['Yr_Mth'] = df['list'].astype(str).apply(''.join)
df.plot(x='Yr_Mth', y=['Moscow', 'San Francisco'], kind='bar', figsize=(25, 75))

plt.title('Temperature Distribution', fontsize=18)
plt.xlabel('Month & Year', fontsize=14)
plt.ylabel('Temperature in inches', fontsize=14)
plt.xticks(rotation=60)
plt.xlim(-1, 24)
plt.grid(True)
plt.savefig("mod5_Q2.jpg")
plt.show()
