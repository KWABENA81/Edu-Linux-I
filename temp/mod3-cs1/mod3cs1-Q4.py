import math


def coord_dict(loc):
    coordinates = dict.fromkeys({'latitude', 'longitude'})
    coordinates['latitude'] = math.radians(loc[0])
    coordinates['longitude'] = math.radians(loc[1])
    return coordinates


def rad_diff(loc0, loc1):
    rad1 = coord_dict(loc0)
    rad2 = coord_dict(loc1)
    return [rad1['latitude'] - rad2['latitude'], rad1['longitude'] - rad2['longitude']]


def gps_distance(location0, location1):
    delta_rad = rad_diff(location0, location1)
    lt_index = 0
    lg_index = 1
    earth_radius = 6373.0

    haversine_formula = math.pow(math.sin(delta_rad[lt_index] / 2), 2) + \
                        math.cos(math.radians(location1[lt_index])) * \
                        math.cos(math.radians(location0[lt_index])) * \
                        math.pow(math.sin(delta_rad[lg_index] / 2), 2)

    gps_dist = 2 * math.atan2(math.sqrt(haversine_formula), math.sqrt(1 - haversine_formula)) * earth_radius
    print('GPS Distance (KM): ', gps_dist)


vancouver = (49.2827, -123.1207)
montreal = (45.5019, -73.5674)
calgary = (51.0447, -114.0719)
toronto = (43.6532, -79.3832)

gps_distance(vancouver, toronto)
gps_distance(toronto, montreal)
