# https://twitter.com/cassidoo/status/1756941571352613116
# https://buttondown.email/cassidoo/archive/youve-got-to-love-whats-yours-alicia-keys/

def from_to(start,end):
    def generator():
        nonlocal start
        if start < end:
            output = start
            start += 1
            return output
    return generator

range = from_to(0,3)

assert range() == 0
assert range() == 1
assert range() == 2
assert range() == None
assert range() == None
