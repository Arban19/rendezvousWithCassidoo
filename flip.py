# https://twitter.com/cassidoo/status/1746797451774758934
# https://buttondown.email/cassidoo/archive/try-and-fail-but-dont-fail-to-try-john-quincy/

array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def flip(array, direction):
    if direction == "vertical":
        return array[::-1]
    if direction == "horizontal":
        return list(map(lambda row: row[::-1],array))

assert flip(array, 'vertical') == [[7,8,9],[4,5,6],[1,2,3]]
assert flip(array, 'horizontal') == [[3,2,1],[6,5,4],[9,8,7]]
assert flip(array, 'unspecified') == None
