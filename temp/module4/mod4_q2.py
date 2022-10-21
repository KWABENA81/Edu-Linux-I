import numpy as np

#       Read from file
data = np.loadtxt('python_mod4/777_m4_datasets_v1.0/SalaryGender.csv', dtype=str, delimiter=',')
arr = np.array(data)
print(arr)
count_female = 0
count_male = 0
phd_list = []
with open('python_mod4/777_m4_datasets_v1.0/SalaryGender.csv', 'r') as input_file:
    for line in input_file:
        #   append phd holders into list
        if line.strip('\n').endswith('1'):
            phd_list.append(line)
            if '0' in line:
                count_female += 1
            else:
                count_male += 1

print('\nPhD count: ', len(phd_list))
print('\nPhD Males: ', count_male)
print('\nPhD Females: ', count_female)
