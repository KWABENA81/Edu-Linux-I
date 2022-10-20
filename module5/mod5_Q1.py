import pandas as pd
from matplotlib import pyplot as plt

#   Read file
hurricanes_data = pd.read_csv('inputs/Hurricanes.csv', dtype=str, delimiter=',')

#   capture headers of table
hurricanes_data.head()
df = pd.DataFrame(hurricanes_data)

year_data = df['Year']
hurricanes_data = df['Hurricanes']

year_header = year_data.head(0)
hurricanes_header = hurricanes_data.head(0)

x_title = year_header.name
y_title = hurricanes_header.name

fig = plt.figure(figsize=(25, 85))
plt.ylabel(y_title)
plt.xlabel(x_title)
plt.xticks(rotation=70)

plt.title('Hurricanes in the US')

plt.bar(year_data[0:101], hurricanes_data[0:101])
plt.savefig("mod5_Q1.jpg")
plt.show()

