import numpy as np
from numpy import random

random_data = np.random.random(30)
print(random_data)

mean_random_data = np.mean(random_data)
print('MEAN:\t', mean_random_data)


# Solution Output:
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q9.py
# [0.85261383 0.4312679  0.38495317 0.15760873 0.48146139 0.78339848
#  0.9494609  0.11247086 0.91587825 0.40701346 0.5786867  0.01854551
#  0.61347119 0.51253252 0.22913811 0.81317203 0.32638566 0.02202538
#  0.327936   0.23523179 0.25636538 0.67005191 0.55954009 0.14301838
#  0.11262225 0.09383825 0.8512022  0.24736388 0.72881117 0.9443151 ]
# MEAN:	 0.4586793476727417
#
# Process finished with exit code 0
