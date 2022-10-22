import numpy as np

darr = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
np_data = np.array(darr)
print(darr)
print(np_data)

nnp_data = np.where(np_data > 5)
print(nnp_data)


# Solution Output
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q6.py
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
# (array([2, 2, 2, 3, 3, 3]), array([0, 1, 2, 0, 1, 2]))
#
# Process finished with exit code 0
