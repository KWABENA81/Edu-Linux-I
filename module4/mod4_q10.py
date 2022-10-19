import numpy as np

data1 = np.arange(0, 10+1)
print('ORIG VALUES:\t', data1)

data1[3:9+1] = np.multiply(data1[3:9+1], -1)

print('NEGATED:\t\t', data1)

#   SOLUTION OUTPUT
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q10.py
# ORIG VALUES:	 [ 0  1  2  3  4  5  6  7  8  9 10]
# NEGATED:		 [ 0  1  2 -3 -4 -5 -6 -7 -8 -9 10]
#
# Process finished with exit code 0
