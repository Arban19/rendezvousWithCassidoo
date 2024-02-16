def from_to(start,end):
    adjusted_start = start - 1
    adjusted_end = end - 1
    def generator():
        nonlocal adjusted_start
        if adjusted_start < adjusted_end:
            adjusted_start += 1
            return adjusted_start
    return generator

range = from_to(0,3)

assert range() == 0
assert range() == 1
assert range() == 2
assert range() == None
assert range() == None
