# https://twitter.com/cassidoo/status/1769626762525175899
# https://buttondown.email/cassidoo/archive/you-can-put-things-off-until-tomorrow-but/

def qualifies(arr):
    if len(arr) < 3:
        return False
    return arr != sorted(arr) and arr != sorted(arr, reverse=True)

def hills(arr):
    if not qualifies(arr):
        return 0
    return sum(1 for i in range(1, len(arr)-1) if arr[i] >= arr[i-1] and arr[i] > arr[i+1])

def valleys(arr):
    if not qualifies(arr):
        return 0
    return sum(1 for i in range(1, len(arr)-1) if arr[i] <= arr[i-1] and arr[i] < arr[i+1])

assert hills([1,2,1]) == 1
assert valleys([1,2,1]) == 0

assert hills([1,0,1]) == 0
assert valleys([1,0,1]) == 1

assert hills([7,6,5,5,4,1]) == 0
assert valleys([7,6,5,5,4,1]) == 0

assert hills([3,4,1,1,6,5]) == 2
assert valleys([3,4,1,1,6,5]) == 1

assert hills([1,2,3,3,4,6]) == 0
assert valleys([1,2,3,3,4,6]) == 0

assert hills([3,4,1,6,6,5]) == 2
assert valleys([3,4,1,6,6,5]) == 1
