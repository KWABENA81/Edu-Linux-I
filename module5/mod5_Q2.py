import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#   Read file
hurricanes_data = pd.read_csv('inputs/CityTemps.csv', dtype=str, delimiter=',')

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)
print('data ', df,'\nllll')
# extract the axis data
x_axis = df['Year'] + '-' + df['Month']

# year_header = year_data.head(0)
x_axis_title = 'Year & Month'
#print('\n\ndata ',x_axis_title)
moscow_data = df['Moscow']
moscow_header = moscow_data.head(0)
#print('moscow_data\n', moscow_data)
sanfrancisco_data = df['San Francisco']
# sanfrancisco_header = sanfrancisco_data.head(0)
# #
# y_data = month_data[0:20]
x_data = moscow_data[0:23]
#print('\n\ndata\n ', x_data)
#
fig = plt.figure(figsize=(25, 75))
# # plt.ylabel(y_axis_title)
# print('y_axis_title\n',df['Year'][0:23])
# print('x_axis_title\n',x_axis_title)
plt.xlabel(x_axis_title)
plt.xticks(rotation=70)
plt.ylabel('Rainfall in inches')
plt.title('Rainfall for San Francisco vs Moscow')
#plt.histtype('bar')
plt.hist(df['Moscow'],histtype='bar',label='str')       #plt.bar(year_data[0:101], hurricanes_data[0:101])
plt.show()
