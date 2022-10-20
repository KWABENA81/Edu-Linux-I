import dask.dataframe as dd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt, pylab

#   Read file
temp_data = pd.read_csv('inputs/Cars2015.csv')
params = {'legend.fontsize': 'medium', 'figure.figsize': (35, 35),
          'axes.labelsize': 'medium', 'axes.titlesize': 'large',
          'xtick.labelsize': 'small', 'ytick.labelsize': 'small'}
pylab.rcParams.update(params)

#   capture headers of table
df = pd.DataFrame(temp_data, columns=['Make', 'Model'])
#   count occurrences of combined columns
occurrences = df['Make'].value_counts().to_dict()
print(occurrences)

makes = list(occurrences.keys())
counts = list(occurrences.values())
plt.pie(counts, labels=makes)
#
plt.title('Count of Model releases by Auto Makers', fontsize=16)
plt.savefig("mod5_Q3.jpg")
plt.show()
