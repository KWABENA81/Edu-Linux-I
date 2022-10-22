import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#   Read file
hurricanes_data = pd.read_csv('inputs/CityTemps.csv', dtype=str, delimiter=',')

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)
print(hurricanes_data)
# extract the axis data
x_axis = df['Year'] + '/' + df['Month']

x_axis_title = 'Month & Year'
# moscow_data = df['Moscow']
# moscow_header = moscow_data.head(0)

fig = plt.figure(figsize=(25, 75))
plt.xlabel(x_axis_title)
plt.xticks(rotation=70)
plt.xlim(-1, 24)
plt.ylim(-10, 25)
plt.grid(True)

x_yr_mth = np.array(x_axis)
y_moscow = np.array(df['Moscow'])

print(y_moscow)
plt.ylabel('Rainfall in inches')
plt.title('Rainfall Distribution in Moscow')

plt.ylabel('Rainfall in inches')
plt.title('Rainfall Distribution')
plt.bar(x_yr_mth, y_moscow)
plt.show()
##############
x_yr_mth = np.array(x_axis)
fig = plt.figure(figsize=(25, 75))
plt.xlabel(x_axis_title)
plt.xticks(rotation=70)
plt.xlim(-1, 24)

plt.grid(True)

y_san_francisco = np.array(df['Moscow'])
plt.title('Rainfall Distribution in San Francisco')
plt.ylabel('Rainfall in inches')
plt.ylim(-10, 25)


y_san_francisco = np.array(df['San Francisco'])
plt.title('Rainfall Distribution in San Francisco')
plt.ylabel('Rainfall in inches')
plt.ylim(5, 30)

print(y_san_francisco)
plt.ylabel('Rainfall in inches')

