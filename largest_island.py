# https://twitter.com/cassidoo/status/1772152158097391951
# https://buttondown.email/cassidoo/archive/the-privilege-of-a-lifetime-is-to-become-who-you/

def largest_island(data):
    rows, cols = len(data), len(data[0])
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if data[i][j] == 1:
                max_area = max(calculate_island_area(data, i, j, rows, cols), max_area)
    return max_area

def calculate_island_area(data, i, j, rows, cols):
    area = 1
    data[i][j] = 0

    if i > 0 and data[i - 1][j] == 1:
        area += calculate_island_area(data, i - 1, j, rows, cols)
    if i < rows - 1 and data[i + 1][j] == 1:
        area += calculate_island_area(data, i + 1, j, rows, cols)
    if j > 0 and data[i][j - 1] == 1:
        area += calculate_island_area(data, i, j - 1, rows, cols)
    if j < cols - 1 and data[i][j + 1] == 1:
        area += calculate_island_area(data, i, j + 1, rows, cols)
    return area
