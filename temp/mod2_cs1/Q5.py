import re
from collections import Counter

var = input("Enter string: ")
letters =''
for i, x in enumerate(var):
    if x.isalpha() and i % 2 == 0:
        letters += x

print('word: ', letters)


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q5.py
# Enter string: hdikss7jkdsd79
# word:  hisks
#
# Process finished with exit code 0
