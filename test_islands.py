from largest_island import largest_island

def test_map1():
    map1 = [
        [0,1,1,1,0,0,0,1,1],
        [0,1,1,1,0,1,0,0,0],
        [0,1,0,0,0,0,0,1,0],
        [0,0,1,1,0,1,1,1,0],
    ]
    assert largest_island(map1) == 7

def test_map2():
    map2 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert largest_island(map2) == 1

def test_map3():
    map3 = [
        [1, 0, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    assert largest_island(map3) == 3

def test_map4():
    map4 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    assert largest_island(map4) == 25
