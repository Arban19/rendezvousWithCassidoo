# https://twitter.com/cassidoo/status/1767084127541449018
# https://buttondown.email/cassidoo/archive/if-you-dont-go-towards-the-thing-you-fear-you/

def max_gap(arr):
    arr.sort()
    if len(arr) < 2:
        return 0
    return max(map(lambda x, y: y - x, arr, arr[1:]))

assert max_gap([]) == 0
assert max_gap([3, 6, 9, 1, 2]) == 3
assert max_gap([-1, -10, -5, -8, -3]) == 3
assert max_gap([-1, 5, -10, 3, -5, -8, -3]) == 4
