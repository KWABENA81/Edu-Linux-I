import numpy as np
from numpy import nan, random

random_data = random.randint(99, size=(10, 10))
print(random_data)

max_num = np.amax(random_data)
print('MAXIMUM:\t', max_num)

min_num = np.amin(random_data)
print('MINIMUM:\t', min_num)


# Solution Output:
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q8.py
# [[45 47 34 87 86 80 50  4 42 28]
#  [57 41 76 39 84 64 67 75 73 26]
#  [61  6 37 67 32  0 78 11 93 49]
#  [24 41  6 72 74 22 78 11 75 34]
#  [23 46 63 89 22 74 82 34 23  1]
#  [98 80 76 42 25 19 23 64 39 83]
#  [86 45 75 29 65 41 65 29 29 53]
#  [14 82 88 70 17 35 39 93 36 71]
#  [51 47 47 97 79 89 12 46  8 25]
#  [49 38 43 52 75  4 51 36 38 40]]
# MAXIMUM:	 98
# MINIMUM:	 0
#
# Process finished with exit code 0
