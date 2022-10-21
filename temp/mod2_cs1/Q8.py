#   list intersection
numbers0 = [1, 3, 6, 78, 35, 55]
numbers1 = [12, 24, 35, 24, 88, 120, 155]

print('number0: ', numbers0)
print('number1: ', numbers1)

numberintersect = []
for x in numbers0:
    if x in numbers1:
        numberintersect.append(x)

print('numberintersect: ', numberintersect)


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q8.py
# number0:  [1, 3, 6, 78, 35, 55, 24]
# number1:  [12, 24, 35, 24, 88, 120, 155]
# numberintersect:  [35, 24]

# ---
# number0:  [1, 3, 6, 78, 35, 55]
# number1:  [12, 24, 35, 24, 88, 120, 155]
# numberintersect:  [35]
#
# Process finished with exit code 0
#
# Process finished with exit code 0
