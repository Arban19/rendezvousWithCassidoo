import math

def rotated_num(numbers):
    min_value = math.inf
    min_indices = []

    for i, num in enumerate(numbers):
        if num < min_value:
            min_value = num
            min_indices = [i]
        elif num == min_value:
            min_indices.append(i)

    return max(min_indices)

assert rotated_num([4, 0, 1, 2, 3]) == 1
assert rotated_num([7, 9, 10]) == 0
assert rotated_num([7, 7, 314, 1337, 7]) == 4
