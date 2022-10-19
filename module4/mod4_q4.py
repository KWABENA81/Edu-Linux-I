import numpy as np

#       Read from file
data = np.loadtxt('python_mod4/777_m4_datasets_v1.0/SalaryGender.csv', dtype=str, delimiter=',')
arr = np.array(data)
print(arr)
count = 0
with open('python_mod4/777_m4_datasets_v1.0/SalaryGender.csv', 'r') as input_file:
    for line in input_file:
        if line.strip('\n').endswith('1'):
            count += 1

print('\nPhD count: ', count)
