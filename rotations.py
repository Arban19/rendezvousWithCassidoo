# https://twitter.com/cassidoo/status/1731574854019666130
# https://buttondown.email/cassidoo/archive/the-best-preparation-for-tomorrow-is-doing-your-9764/

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
assert rotated_num([5, 4, 3, 2, 1, 0, -1, 6]) == 6
