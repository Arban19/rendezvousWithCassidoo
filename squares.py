def squares(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    return sum(i ** 2 for i in range(1, n + 1))

assert squares(5) == 55
assert squares(10) == 385
assert squares(25) == 5525
assert squares(100) == 338350
