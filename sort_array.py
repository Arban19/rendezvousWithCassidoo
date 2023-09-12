def separateAndsort(numbers):
    odd = []
    even = []

    for number in numbers:
        if isinstance(number,int):
            if number != 0:
                if number % 2 == 0:
                    even.append(number)
                else:
                    odd.append(number)

    even.sort()
    odd.sort()

    return even, odd

assert separateAndsort([0,1,2,3,4,5]) == ([2,4], [1,3,5])
assert separateAndsort([0,0,0,0,0]) == ([], [])
assert separateAndsort([4,3,2,1,5,7,8,9]) == ([2,4,8], [1,3,5,7,9])
assert separateAndsort(["a","b","c"]) == ([], [])
assert separateAndsort([1,"a","","s"]) == ([],[1])
assert separateAndsort([-2,-3,-4,-5,-6]) == ([-6,-4,-2], [-5,-3])
assert separateAndsort([10,-3,7,-2,1]) == ([-2,10], [-3,1,7])
