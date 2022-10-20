import numpy as np

int_arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print(int_arr)

counts_list = []
for x in range(len(int_arr)):
    a = int_arr[x]
    counts_list.append(np.count_nonzero(int_arr == a))

print(counts_list)


#SOLUTION RUN:
# /home/sask/Documents/edureka-py/edureka-python-scripting/module4/venv/bin/python /home/sask/Documents/edureka-py/edureka-python-scripting/module4/mod4_q5.py
# [0 5 4 0 4 4 3 0 0 5 2 1 1 9]
# [4, 2, 3, 4, 3, 3, 1, 4, 4, 2, 1, 2, 2, 1]
#
# Process finished with exit code 0
