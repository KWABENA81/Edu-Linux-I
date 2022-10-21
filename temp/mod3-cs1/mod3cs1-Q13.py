import math


def cods(loc):
    coords = dict.fromkeys({'latitude', 'longitude'})
    coords['latitude'] = loc[0]
    coords['longitude'] = loc[1]
    return coords


def codsDiff(locA, locB):
    cods1 = cods(locA)
    cods2 = cods(locB)
    listk = [cods1['latitude'] - cods2['latitude'], cods1['longitude'] - cods2['longitude']]
    print(listk)
    return listk


def distance_between(locA, locB):
    coordDiff = codsDiff(locA, locB)
    # coordB = cods(locB)
    lat = 0
    lon = 1
    conversion_factor = 6373.0

    print(coordDiff[lat], ' coordDiff[lat]: ', coordDiff[lon])
    a = math.pow(math.sin(coordDiff[lat] / 2), 2)
    d = math.pow(math.sin(coordDiff[lon] / 2), 2)
    print(' a: ', a)
    b = math.cos(locB[0])
    print(' b: ', locB[0])
    print(' b=: ', b)
    c = math.cos(locA[0])
    print(' c: ', locA[0])
    print(' c=: ', c)

    print(' d: ', d)
    result1 = a + b * c * d
    print(' result1: ', result1)
    result2 = conversion_factor * (2 * math.atan2(math.sqrt(result1), math.sqrt(1 - result1)))
    print('distance_between result2 : ', result2)


vancouver = (49.2827, -123.1207)
montreal = (45.5019, -73.5674)
calgary = (51.0447, -114.0719)
toronto = (43.6532, -79.3832)

#distance_between(toronto, vancouver)
distance_between(toronto, montreal)
