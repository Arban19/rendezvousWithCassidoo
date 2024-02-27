# https://twitter.com/cassidoo/status/1762023522241573185
# https://buttondown.email/cassidoo/archive/the-potential-for-greatness-lives-within-each-of/

import math

def remove_digit(numbers, digit):
    str_dgt, str_nums = str(digit), str(numbers)
    z = -math.inf
    for n in range(len(str(numbers))):
        if str_nums[n] == str_dgt:
            z = max(int(str_nums[:n] + str_nums[n+1:]), z)
    return z

assert remove_digit(123451, 1) == 23451
assert remove_digit(31415926, 1) == 3415926
assert remove_digit(1231, 1) == 231
assert remove_digit(121212, 2) == 12121
