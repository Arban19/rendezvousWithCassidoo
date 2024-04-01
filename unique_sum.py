# https://twitter.com/cassidoo/status/1774686751686045751
# https://buttondown.email/cassidoo/archive/all-we-have-to-decide-is-what-to-do-with-the-time-1254/

def unique_sum(arr):
    return sum(num for num in arr if len(set(str(num))) == len(str(num)))

assert unique_sum([1,2,3]) == 6
assert unique_sum([11,22,33]) == 0
assert unique_sum([101,2,3]) == 5
