# https://twitter.com/cassidoo/status/1762023522241573185
# https://buttondown.email/cassidoo/archive/the-potential-for-greatness-lives-within-each-of/

import math

def remove_digit(numbers, digit):
    nums, max_num = str(numbers), -math.inf
    for n in range(len(nums)):
        if nums[n] == str(digit):
            max_num = max(int(nums[:n] + nums[n+1:]), max_num)
    return max_num if max_num != -math.inf else numbers

assert remove_digit(31415926, 1) == 3415926
assert remove_digit(1231, 1) == 231
assert remove_digit(281881, 8) == 28181
assert remove_digit(100,2) == 100
