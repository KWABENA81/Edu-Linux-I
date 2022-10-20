from numpy import random

nums = random.randint(19, size=(4, 4))
print('Original: \n', nums)

nums[[0, 3]] = nums[[3, 0]]
print('Swapped:\n', nums)

# Solution Output:
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q13.py
# Original:
#  [[ 8  0  7  7]
#  [ 6 10  7 16]
#  [ 0  4 11 18]
#  [ 1  6 11 10]]
# Swapped:
#  [[ 1  6 11 10]
#  [ 6 10  7 16]
#  [ 0  4 11 18]
#  [ 8  0  7  7]]
#
# Process finished with exit code 0