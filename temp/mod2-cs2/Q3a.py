import re
from collections import Counter

#   uname = input("Enter username: ")
passwd = input("Enter password: ")
result = True

if re.search(r'\s', passwd) :
    result = False
    exit
if result:
    if not len(passwd) == 12:
        result = False
    else:
        if not re.search(r'[a-z|A-Z|0-9]{12}', passwd):
            result = False

print(' IS PASSWORD VALID ', result)


