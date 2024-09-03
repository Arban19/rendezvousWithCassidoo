def max_pairs(pairs):
    left_collection = {}
    right_collection = {}

    for pair in pairs:
        direction, size = pair.split("-")

        if direction == "L":
            if size in left_collection:
                left_collection[size] += 1
            else:
                left_collection[size] = 1
        
        elif direction == "R":
            if size in right_collection:
                right_collection[size] += 1
            else:
                right_collection[size] = 1    

    return calculate_overlap(left_collection, right_collection)

def calculate_overlap(left_collection, right_collection):
    return sum(min(left_collection.get(size, 0), right_collection.get(size, 0)) for size in left_collection)

assert max_pairs(["L-10","R-10","L-11","R-10","L-10","R-11"]) == 3
assert max_pairs(["L-10","L-11","L-12","L-13"]) == 0
assert max_pairs(["L-8","L-8","L-8","R-8"]) == 1
assert max_pairs(["L-8","R-8","R-8","R-8"]) == 1
