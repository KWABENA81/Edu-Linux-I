
var = input("Enter number: ")
if var.isdecimal():
    number = int(var)
    floatsum = 0.0
    if number > 0:
        for n in range(1, number+1):
            floatsum += n / (n + 1)
    print(floatsum)



#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q14.py
# Enter number: 6
# 4.4071428571428575
#
# Enter number: 5
# 3.5500000000000003

