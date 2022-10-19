import numpy as np

#       Read from file
data = np.loadtxt('python_mod4/777_m4_datasets_v1.0/SalaryGender.csv', dtype=str, delimiter=',')
arr = np.array(data)
print(arr)

col_0 = [row[0] for row in arr]
print('Column 1:\n', col_0)

col_1 = [row[1] for row in arr]
print('Column 2:\n', col_1)

col_2 = [row[2] for row in arr]
print('Column 3:\n', col_2)

col_3 = [row[3] for row in arr]
print('Column 4:\n', col_3)
