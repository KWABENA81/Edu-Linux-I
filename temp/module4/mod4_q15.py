import numpy as np
import pandas as pd
from numpy import random

MathScoreTerm1 = np.loadtxt('python_mod4/777_m4_datasets_v1.0/MathScoreTerm1.csv', dtype=str, delimiter=',')
arr_MathScoreTerm1 = np.array(MathScoreTerm1)
df_MathScoreTerm1 = pd.DataFrame(MathScoreTerm1)
print('MathScore Term 1\n', df_MathScoreTerm1)

PhysicsScoreTerm1 = np.loadtxt('python_mod4/777_m4_datasets_v1.0/PhysicsScoreTerm1.csv', dtype=str, delimiter=',')
arr_PhysicsScoreTerm1 = np.array(PhysicsScoreTerm1)
df_PhysicsScoreTerm1 = pd.DataFrame(PhysicsScoreTerm1)
print('Physics Score Term 1\n', df_PhysicsScoreTerm1)

DSScoreTerm1 = np.loadtxt('python_mod4/777_m4_datasets_v1.0/DSScoreTerm1.csv', dtype=str, delimiter=',')
arr_DSScoreTerm1 = np.array(DSScoreTerm1)
df_DSScoreTerm1 = pd.DataFrame(DSScoreTerm1)
print('DS Score Term 1\n', df_DSScoreTerm1)

middle_tn_schools = np.loadtxt('python_mod4/777_m4_datasets_v1.0/middle_tn_schools.csv', dtype=str, delimiter=',')
arr_middle_tn_schools = np.array(middle_tn_schools)
df_middle_tn_schools = pd.DataFrame(middle_tn_schools)
print('Middle TN Schools\n'.upper(), df_middle_tn_schools)

ScoreFinal = np.loadtxt('python_mod4/777_m4_datasets_v1.0/ScoreFinal.csv', dtype=str, delimiter=',')
arr_ScoreFinal = np.array(ScoreFinal)
df_ScoreFinal = pd.DataFrame(ScoreFinal)
print('Score Final\n', df_ScoreFinal)
