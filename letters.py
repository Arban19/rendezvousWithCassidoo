# https://twitter.com/cassidoo/status/1744263422873678112
# https://buttondown.email/cassidoo/archive/the-most-effective-way-to-do-it-is-to-do-it-5924/

from itertools import permutations

def letters(list_of_strs):
    perms = []
    l = len(list_of_strs)
    for i in range(1, l+1):
        perms += list(permutations(list_of_strs,i))
    result = set(perms)
    res = ""
    final_result = list(map(res.join,result))
    print(sorted(final_result, key=len, reverse=False))
    return len(final_result)

assert letters("X") == 1
assert letters(["A","A","B"]) == 8
