import pandas as pd
from matplotlib import pyplot as plt

#   Read file
hurricanes_data = pd.read_csv('Hurricanes.csv', dtype=str, delimiter=',')

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)

year_data = df['Year']
hurricanes_data = df['Hurricanes']

year_header = year_data.head(0)
hurricanes_header = hurricanes_data.head(0)

x_title = year_header.name
y_title = hurricanes_header.name

x_data = year_data[0:100]
y_data = hurricanes_data[0:100]

fig = plt.figure(figsize=(25, 75))
plt.ylabel(y_title)
plt.xlabel(x_title)
plt.title('Hurricanes in the US')

plt.bar(x_data, y_data)
plt.show()

