inputStr = 'abcdefgabc'

#   create initialize dictionary with zero values
dict = {}.fromkeys(inputStr, 0)

for x in inputStr:
    dict[x] = dict[x] + 1

print(dict)


# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q7.py
# {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
#
# Process finished with exit code 0