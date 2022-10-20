import pandas as pd
from matplotlib import pyplot as plt

#   Read file
hurricanes_data = pd.read_csv('Cars2015.csv', dtype=str, delimiter=',')

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)
print(df)
#
year_data = df['Year']
month_data = df['Month']
moscow_data = df['Moscow']
melbourne_data = df['Melbourne']
sanfrancisco_data = df['San Francisco']

year_header= year_data.head(0)
month_header = month_data.head(0)
moscow_header= moscow_data.head(0)
melbourne_header = melbourne_data.head(0)
sanfrancisco_header = sanfrancisco_data.head(0)

y_title = year_header.name
x_title = month_header.name

x_data = month_data[0:24]
y_data = year_data[0:24]
#
fig = plt.figure(figsize=(25, 75))
plt.ylabel(y_title)
plt.xlabel(x_title)
plt.title('Rain fall')
#
plt.hist(x_data, y_data)
plt.show()



