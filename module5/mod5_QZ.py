import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#   Read file
df = pd.DataFrame({'Year': ['2014', '2015'], 'quarter': ['q1', 'q2']})
print('\ndf1\n', df)
df['list'] = df[['Year', 'quarter']].values.tolist()
print('\ndf2\n', df['list'])
df['period'] = df['list'].apply(''.join)
print('\ndf3\n', df)

temp_data = pd.read_csv('inputs/CityTemps.csv')
#   capture headers of table
data = temp_data.head()
df = pd.DataFrame(data, columns=['Year', 'Month', 'Moscow', 'San Francisco'])
df['list'] = df[['Year', 'Month']].values.tolist()
df['Yr_Mth'] = df['list'].astype(str).apply(''.join)
print('\ndf6\n', df)
# extract the axis data
# x_axis = df['Month'] + '-' + df['Year']
# x=df['Year'].merge(df['Month'])
# #df['x'] = df.Year.astype(str).str.cat(df.Month.astype(str), sep='-')
# df.plot(x, y=['Moscow', 'San Francisco'], kind='bar', figsize=(25, 75))
