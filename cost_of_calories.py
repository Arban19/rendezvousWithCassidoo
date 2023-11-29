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

z = combos(zip_items(calories,prices))
for combo in z:
    print(combo)

# def combo_meets_requirement(items):
#     for items[0] in items:
#         return sum(items[0])

# def min_cost_for_calories(calories, prices, daily_goal):
#     z = combos(list(zip(calories,prices)))
#     filter(,z)



# combinations_list = [(comb, tuple(calories[i] for i in comb)) for i in range(1, len(calories) + 1) for comb in combinations(range(len(calories)), i)]
# print("Number of combinations:", len(combinations_list))
# print("Combinations:")

# while daily_goal > elements in combinations_list:
#     for indices, elements in combinations_list:

#         print(f"Indices: {indices}, Elements: {elements}")
