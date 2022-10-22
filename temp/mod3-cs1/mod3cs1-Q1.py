import math


def distance_from_origin(up, down, left, right):
    dist_tuple = {'UP': up, 'DOWN': down, 'LEFT': left, 'RIGHT': right}
    y = dist_tuple['UP'] - dist_tuple['DOWN']
    x = dist_tuple['RIGHT'] - dist_tuple['LEFT']

    dist_from_origin = math.sqrt(math.pow(y, 2) + math.pow(x, 2))
    print('UP    ', dist_tuple['UP'])
    print('DOWN  ', dist_tuple['DOWN'])
    print('LEFT  ', dist_tuple['LEFT'])
    print('RIGHT ', dist_tuple['RIGHT'])
    print('Current distance from origin: ', dist_from_origin)


distance_from_origin(5, 3, 3, 2)

# UP     5
# DOWN   3
# LEFT   3
# RIGHT  2
# Current distance from origin:  2.23606797749979
#
# Process finished with exit code 0
