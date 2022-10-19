import numpy as np
import pandas as pd
from numpy import random
from openpyxl.utils import dataframe

# file_mst = open('MathScoreTerm1_out.txt', 'w')
#
MathScore = np.loadtxt('MathScoreTerm1.csv', dtype=str, delimiter=',')
arr_MathScore = np.array(MathScore)
df_MathScore = pd.DataFrame(MathScore)
# print('#1.\tRead Math Scores:\n', df_MathScore)

df_MathScore_filtered = df_MathScore[[1, 2, 4, 5, 6]]
# print('#2.\tMath Score\n', df_MathScore_filtered)

df_MathScore_filtered_Zero_score = df_MathScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tMath Scores without blank scores\n', df_MathScore_filtered_Zero_score)
# ===========

PhysicsScore = np.loadtxt('PhysicsScoreTerm1.csv', dtype=str, delimiter=',')
arr_PhysicsScore = np.array(PhysicsScore)

df_PhysicsScore = pd.DataFrame(PhysicsScore)
# print('#1.\tRead Physics Scores:\n', df_PhysicsScore)

df_PhysicsScore_filtered = df_PhysicsScore[[1, 2, 4, 5, 6]]
# print('#2.\tPhysics Scores without Names & Ethnicity\n', df_PhysicsScore_filtered)

df_PhysicsScore_filtered_Zero_score = df_PhysicsScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tPhysics Scores without blank scores\n', df_PhysicsScore_filtered_Zero_score)
# ===========


DSScore = np.loadtxt('DSScoreTerm1.csv', dtype=str, delimiter=',')
arr_DSScore = np.array(DSScore)

df_DSScore = pd.DataFrame(DSScore)
# print('#1.\tRead DS Scores:\n', df_DSScore)

df_DSScore_filtered = df_DSScore[[1, 2, 4, 5, 6]]
# print('#2.\tDS Scores without Names & Ethnicity\n', df_DSScore_filtered)

df_DSScore_filtered_Zero_score = df_DSScore_filtered.replace(r'^\s*$', 0, regex=True)
print('#3.\tDS Scores without blank scores\n', df_DSScore_filtered_Zero_score)

# Swap M/F for 1/2
temp_df = df_MathScore_filtered_Zero_score.replace(r'^M$', 1, regex=True)
df_MathScore_filtered_Zero_score = temp_df.replace(r'^F$', 2, regex=True)

df_concat1_2 = pd.concat([df_MathScore_filtered_Zero_score, df_PhysicsScore_filtered_Zero_score[[1, 4]]], axis=1)
print('#4.\tConcat 1 & 2 scores\n', df_concat1_2)

df_concat_1_2_3 = pd.concat([df_concat1_2, df_DSScore_filtered_Zero_score[[1, 4]]], axis=1)
print('#4.\tConcat 1 & 2 & 3 scores\n', df_concat_1_2_3)

#   Write into file
df_concat_1_2_3.to_csv(r'ScoreFinal.csv', header=None, index=None, sep=',', mode='a')
