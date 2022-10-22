import re
from collections import Counter

uname = input("Enter username: ")
passwd = input("Enter password: ")
result = True

if re.search(r'\s', passwd) or re.search(r'\s', uname):
    result = False
    print(' BAD CHARACTERS')
    exit
if result:
    if 6 > len(passwd) or len(passwd) > 12:
        result = False
        print(' INVALID LENGTH', len(passwd))
    else:
        if not re.search(r'[a-z]{1}', passwd):
            result = False
            print(" INVALID small", passwd)
        else:
            print(' VALID ', passwd)
            if re.search(r'[A-Z]{1}', passwd):
                print(' VALID CAPS', passwd)
                if re.search(r'[0-9]{1}', passwd):
                    print(' VALID digits', passwd)
                    if re.search(r'[$#@]{1}', passwd):
                        print(' VALID Characters', passwd)
                    else:
                        result = False
                        print(' INVALID Characters', passwd)
                else:
                    result = False
                    print(' INVALID digits', passwd)
            else:
                result = False
                print(' INVALID CAPS', passwd)

print(' IS PASSWORD VALID ', result)



# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q3.py
# Enter username: kldklks
# Enter password: jhu 99LK$
#  BAD CHARACTERS
#  IS PASSWORD VALID  False
#
# Process finished with exit code 0
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q3.py
# Enter username: hutgys
# Enter password: Ags$65hdj
#  VALID  Ags$65hdj
#  VALID CAPS Ags$65hdj
#  VALID digits Ags$65hdj
#  VALID Characters Ags$65hdj
#  IS PASSWORD VALID  True
#
# Process finished with exit code 0