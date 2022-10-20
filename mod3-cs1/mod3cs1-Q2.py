data_list = [x * 7 for x in range(12)]
print(data_list)


def find_data(dlist, param):
    found = False
    for y in dlist:
        if y == param:
            found = True
            break
    return found


print(find_data(data_list, 561))
