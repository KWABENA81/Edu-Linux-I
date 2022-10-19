import numpy as np
from numpy import random

nums = random.randint(19, size=(4, 8))
print('Original: \n', nums)

nums_rank = np.linalg.matrix_rank(nums)
print('\nRank:\n', nums_rank)


# Solution Output
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q14.py
# Original:
#  [[ 9  1 12 17  8 10  0 11]
#  [ 3  4 11  1  9 11 11 18]
#  [11  2  3  3 15 13  5 16]
#  [ 9 10 18  6  3  2  5  0]]
#
# Rank:
#  4
#
# Process finished with exit code 0