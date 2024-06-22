# https://twitter.com/cassidoo/status/1703653007013896654
# https://buttondown.email/cassidoo/archive/let-us-remember-that-our-voice-is-a-precious-gift/

def build_stair_case(n: int):
    steps = 0
    req_blocks = 0

    while req_blocks < n:
        steps += 1
        req_blocks += 1
        n -= req_blocks
    return steps

assert build_stair_case(0) == 0
assert build_stair_case(1) == 1
assert build_stair_case(2) == 1
assert build_stair_case(3) == 2
assert build_stair_case(5) == 2
assert build_stair_case(6) == 3
assert build_stair_case(9) == 3
