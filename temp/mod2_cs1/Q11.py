import random

numbers = [12, 24, 35, 70, 88, 120, 155]
#   delete  index 0, 4, 5
print('original: ',numbers)
for x in numbers:
    ind = numbers.index(x)
    if ind == 5 or ind == 4 or ind == 0:
        del numbers[ind]
print('final 1: ',numbers)


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q11.py
# original:  [12, 24, 35, 70, 88, 120, 155]
# final 1:  [24, 35, 70, 88, 155]
#
# Process finished with exit code 0
