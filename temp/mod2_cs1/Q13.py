import random

maxnum = 1000
minnum = 1
var = random.randint(minnum, maxnum+1)
print('Random number: ', var)
for x in range(1, var):

    if x % 5 == 0 and x % 7 == 0:
        print(x)


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q13.py
# Random number:  115
# 35
# 70
# 105

# Random number:  507
# 35
# 70
# 105
# 140
# 175
# 210
# 245
# 280
# 315
# 350
# 385
# 420
# 455
# 490


