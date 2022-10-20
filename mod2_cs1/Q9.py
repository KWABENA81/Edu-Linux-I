#   remove duplicates
nlist = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(nlist)

nlist.sort(reverse=True)
nlistunique = []
for x in nlist:
    if x not in nlistunique:
        nlistunique.append(x)

print(nlistunique)


#   OUTPUT
# /home/sasops/Documents/ops/edureka-python-scripting/python_edureka/bin/python /home/sasops/PycharmProjects/python_edureka/DS_mod2/Q9.py
# [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# [155, 120, 88, 35, 24, 12]
#
# Process finished with exit code 0
