calories = [200, 400, 600, 800]
prices = [50, 60, 80, 100]
daily_goal = 1200

from itertools import combinations

def zip_items(calories,prices):
    output = []
    for i in range(len(calories)):
        c = calories[i]
        p = prices[i]
        output.append({"calories":c,"price":p})
    return output

# y = zip_items(calories,prices)

def combos(items):
    all_combos = []
    for i in range(len(items)+1):
        all_combos += combinations(items,i)
    return all_combos

# z = combos(y)
# for a_combo in z:
#     print(a_combo)

def sum_of_calories(combo):
    result = 0
    for item in combo:
        result += item["calories"]
    return result

# for a_combo in z:
#     print(sum_of_calories(a_combo))

def min_cost_for_calories(calories, prices, daily_goal):
    cost = []
    food_items = zip_items(calories,prices)
    food_items_combos = combos(food_items)
    valid_combos = filter(lambda combo: sum_of_calories(combo) >= daily_goal,food_items_combos)
    for each_combo in valid_combos:
        cost_per_combo = 0
        for food_item in each_combo:
            cost_per_combo += (food_item["price"])
        cost.append(cost_per_combo)
    return min(cost)

print(min_cost_for_calories(calories,prices,1200))
