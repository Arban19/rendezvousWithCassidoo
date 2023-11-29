from itertools import combinations

calories = [200, 400, 600, 800]
prices = [50, 60, 80, 100]

def zip_items(calories,prices):
    output = []
    for i in range(len(calories)):
        c = calories[i]
        p = prices[i]
        output.append({"calories":c,"price":p})
    return output

def combos(items):
    all_combos = []
    for i in range(len(items)+1):
        all_combos += combinations(items,i)
    return all_combos

def sum_of_calories(combo):
    result = 0
    for item in combo:
        result += item["calories"]
    return result

def min_cost_for_calories(calories, prices, daily_goal):
    cost = []
    food_items = zip_items(calories,prices)
    food_items_combos = combos(food_items)
    valid_combos = filter(lambda c: sum_of_calories(c) >= daily_goal, food_items_combos)

    for each_combo in valid_combos:
        cost_per_combo = 0
        for food_item in each_combo:
            cost_per_combo += food_item["price"]
        cost.append(cost_per_combo)
    try:
        return min(cost)
    except ValueError:
        return -1

assert min_cost_for_calories(calories,prices,1200) == 160
assert min_cost_for_calories(calories,prices,40000) == -1
