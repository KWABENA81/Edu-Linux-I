import os
import shutil

import numpy as np
import pandas as pd

data_file = 'python_mod4/777_m4_datasets_v1.0/SalaryGender.csv'
data = pd.read_csv(data_file)
print('DATA\n', data)

df = pd.DataFrame(data)
df2 = df[["Age", "PhD"]]
print('DATA - AGE & PhD\n', df2)

data_file2 = 'SalaryGender_tmp.csv'
#   copy file
shutil.copy(data_file, data_file2)

with open(data_file, 'r') as input_file:
    with open(data_file2, 'w') as output_file:
        for line in input_file:
            if line.strip('\n').endswith('1') or line.strip('\n').endswith('PhD'):
                output_file.write(line)

# replace file
os.replace(data_file2, 'SalaryGender_q3_soln.csv')
