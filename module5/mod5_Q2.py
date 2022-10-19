import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#   Read file
temp_data = pd.read_csv('inputs/CityTemps.csv')

#   capture headers of table
data = temp_data.head()
df = pd.DataFrame(data, columns=['Year' + '-' + 'Month', 'Moscow', 'San Francisco'])

# extract the axis data
# x_axis = df['Month'] + '-' + df['Year']
df.plot(x='Year' + '-' + 'Month', y=['Moscow', 'San Francisco'], kind='bar', figsize=(25, 75))
# df.plot(x='YearMonth', y=['Moscow', 'San Francisco'], kind='bar', figsize=(25, 75))

x_axis_title = 'Month & Year'
# moscow_data = df['Moscow']
# moscow_header = moscow_data.head(0)
#
# # y_data = moscow_data[0:23] print('\n\ndata\n ', y_data)

plt.xlabel(x_axis_title)
plt.xticks(rotation=50)
plt.xlim(-1, 24)
plt.grid(True)
#
plt.ylabel('Temperature in inches')
plt.title('Temperature Distribution')
plt.show()
