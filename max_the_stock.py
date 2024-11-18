def max_the_stock(prices):
    buy_price = prices[0]
    profit = 0

    for price in prices[1:]:
        profit = max(profit, price - buy_price)
        buy_price = min(buy_price, price)
    return profit

assert max_the_stock([7, 1, 5, 3, 6, 4]) == 5
assert max_the_stock([7, 6, 4, 3, 1]) == 0
assert max_the_stock([7, 2, 5, 3, 6, 4, 1]) == 4