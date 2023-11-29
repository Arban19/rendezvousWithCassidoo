calories = [200, 400, 600, 800]
prices = [50, 60, 80, 100]
daily_goal = 1200

def zip_items(calories,prices):
    output = []
    for i in range(len(calories)):
        c = calories[i]
        p = prices[i]
        output.append({"calories":c,"prices":p})
    return output

from itertools import combinations

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

z = combos(zip_items(calories,prices))
for combo in z:
    print(sum_of_calories(combo))

def min_cost_for_calories(calories, prices, daily_goal):
    z = combos(zip_items(calories,prices))
    valid_combos = filter(lambda combo: sum_of_calories(combo) >= daily_goal,z)
    prices = []
    for combo in valid_combos:
        for item in combo:
            result.append(item["prices"])
    return min([prices])

min_cost_for_calories(calories,prices,1200)
