# https://buttondown.com/cassidoo/archive/stand-for-something-or-you-will-fall-for-anything/

def see_buildings_left(buildings):
    highest_building, count_of_buildings = 0, 0

    for building in buildings:
        if building > highest_building:
            count_of_buildings += 1
            highest_building = building

    return count_of_buildings

assert see_buildings_left([1, 2, 3, 4, 5]) == 5
assert see_buildings_left([5, 4, 3, 2, 1]) == 1
assert see_buildings_left([3, 7, 8, 3, 6, 1]) == 3
