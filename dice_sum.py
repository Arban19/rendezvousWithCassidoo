# https://twitter.com/cassidoo/status/1777242062091665749
# https://buttondown.email/cassidoo/archive/7-you-have-to-care-about-your-work-but-not-about/

from itertools import product

def dice_sum(n, m, target):
    faces = range(1, m + 1)
    return sum(1 for combo in product(faces, repeat=n) if sum(combo) == target)

assert dice_sum(1, 6, 3) == 1
assert dice_sum(2, 6, 7) == 6
