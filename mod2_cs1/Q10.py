import random

numbers = [12, 24, 35, 24, 88, 120, 155]
#
print('original: ', numbers)
for x in numbers:
    if x == 24:
        numbers.remove(x)
        continue

print('final: ', numbers)

#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q10.py
# original:  [12, 24, 35, 24, 88, 120, 155]
# final 1:  [12, 35, 88, 120, 155]
#
# Process finished with exit code 0

