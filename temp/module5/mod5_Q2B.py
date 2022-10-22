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
#
fig = plt.figure(figsize=(25, 75))
plt.xlabel(x_axis_title)
plt.xticks(rotation=70)
plt.xlim(-1, 24)
plt.ylim(5, 30)
plt.grid(True)

x_yr_mth = np.array(x_axis)
y_san_francisco = np.array(df['San Francisco'])
print(y_san_francisco)
plt.ylabel('Rainfall in inches')
plt.title('Rainfall Distribution in San Francisco')

plt.bar(x_yr_mth, y_san_francisco, color='green', width=.75)
# plt.hist(y_san_francisco)
plt.show()
