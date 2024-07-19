def increasing_subsequence(numbers):
    lengths, current_length = [], 1
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i + 1]:
            current_length += 1
        else:
            lengths.append(current_length)
            current_length = 1
    lengths.append(current_length)
    return max(lengths)

assert increasing_subsequence([10,9,2,3,7,101,18]) == 4
assert increasing_subsequence([4,4,4,4,3]) == 1
assert increasing_subsequence([10,9,2,3,7,101,18,5,6,7,1,2,3,4,5,6,7]) == 7