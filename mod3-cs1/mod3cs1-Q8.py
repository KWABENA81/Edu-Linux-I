import math

dvalue = input("Enter value of D: ")
dlist = dvalue.split(',', maxsplit=3)
C = 50
H = 30
ndlist = ''

for v in range(0, len(dlist)):
    D = int(dlist[v])
    num = 2 * C * D / H
    Q = int(math.sqrt(num))

    if len(ndlist) != 0:
        ndlist += ','
    ndlist += str(Q)

print(ndlist)

# /usr/bin/python3.10 /home/sask/Documents/edureka/edureka-python-scripting/mod3-cs1/mod3cs1-Q8.py
# Enter value of D: 100,150,180
# 18,22,24
