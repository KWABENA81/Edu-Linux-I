import random

numbers = [12, 24, 35, 70, 88, 120, 155]
numbers2 = []
for x in numbers:
    if x % 5 == 0 and x % 7 == 0:
        continue
    else:
        numbers2.append(int(x))
print('option 1: ',numbers2)

print('option,,, 2: ', [y for y in numbers if y % 5 != 0 or y % 7 != 0])


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q12.py
# option 1:  [12, 24, 88, 120, 155]
# option,,, 2:  [12, 24, 88, 120, 155]
#
# Process finished with exit code 0