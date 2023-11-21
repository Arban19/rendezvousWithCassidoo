def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    for i in range(3,x,2):
        if x % i == 0:
            return False
    return True

def between_numbs(x,y,instruction):
    start, end = min(x,y), max(x,y)
    result = []
    for i in range(start,end+1):
        if instruction == "even" and i%2 == 0:
            result.append(i)
        elif instruction == "odd" and i%2 != 0:
            result.append(i)
        elif instruction == "prime" and is_prime(i):
            result.append(i)

    return result

assert between_numbs(3,11,"even") == [4,6,8,10]
assert between_numbs(15,1,"prime") == [2,3,5,7,11,13]
assert between_numbs(10,2,"odd") == [3,5,7,9]
assert between_numbs(1, 10, "even") == [2, 4, 6, 8, 10]
assert between_numbs(20, 30, "odd") == [21, 23, 25, 27, 29]
assert between_numbs(40, 50, "prime") == [41, 43, 47]
assert between_numbs(5, 5, "even") == []
