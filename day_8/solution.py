import numpy as np
import itertools
grid = []
with open('input.txt', "r") as file:
    for line in file.readlines():
        grid.append(list(line.strip()))
# step 1: get the dimensions
max_x = len(grid)
max_y = len(grid[0])

# step 2: construct the dictionary of frequencies

freq = {}
for x in range(max_x):
    for y in range(max_y):
        if grid[x][y] != ".":
            f = grid[x][y]
            if f not in freq:
                freq[f] = {(x,y)}
            else:
                freq[f].add((x,y))
# step 3: create a grid of possible anti-frequencies
def generate_anti_freq(p1, p2):
    # generate vector between the two points
    x_1, y_1 = p1
    x_2, y_2 = p2
    # points from p1 to p2
    vec_1 = (x_2 - x_1, y_2 - y_1)
    anti_freq_1 = np.subtract(p1, vec_1)
    anti_freq_2 = np.add(p2, vec_1)
    return tuple(anti_freq_1), tuple(anti_freq_2)
anti_freq = [[False for y in range(max_y)] for x in range(max_x)]
for f in freq:
    combinations = itertools.combinations(freq[f], 2)
    for c in combinations:
        p1, p2 = c
        anti_freq_1, anti_freq_2 = generate_anti_freq(p1, p2)
        # check if the anti_freq_1 and anti_freq_2 are within the grid
        if 0 <= anti_freq_1[0] < max_x and 0 <= anti_freq_1[1] < max_y:
            anti_freq[anti_freq_1[0]][anti_freq_1[1]] = True
        if 0 <= anti_freq_2[0] < max_x and 0 <= anti_freq_2[1] < max_y:
            anti_freq[anti_freq_2[0]][anti_freq_2[1]] = True

# get number of slots set to true
count = 0
for x in range(max_x):
    for y in range(max_y):
        if anti_freq[x][y]:
            count += 1

print(f"number of anti_freqs: (Part 1) {count}")

# PART 2

def generate_anti_freq_2(p1, p2, max_x, max_y, anti_freq):
    # generate vector between the two points
    x_1, y_1 = p1
    x_2, y_2 = p2
    anti_freq[x_1][y_1] = True
    anti_freq[x_2][y_2] = True
    vec_1 = (x_2 - x_1, y_2 - y_1)
    decrease_point = np.subtract(p1, vec_1)
    while 0 <= decrease_point[0] < max_x and 0 <= decrease_point[1] < max_y:
        anti_freq[decrease_point[0]][decrease_point[1]] = True
        decrease_point = np.subtract(decrease_point, vec_1)
    increase_point = np.add(p2, vec_1)
    while 0 <= increase_point[0] < max_x and 0 <= increase_point[1] < max_y:
        anti_freq[increase_point[0]][increase_point[1]] = True
        increase_point = np.add(increase_point, vec_1)
    return anti_freq

max_x = len(grid)
max_y = len(grid[0])
anti_freq = [[False for y in range(max_y)] for x in range(max_x)]
for f in freq:
    combinations = itertools.combinations(freq[f], 2)
    for c in combinations:
        p1, p2 = c
        anti_freq = generate_anti_freq_2(p1, p2, max_x, max_y, anti_freq)

# get number of slots set to true
count = 0
for x in range(max_x):
    for y in range(max_y):
        if anti_freq[x][y]:
            count += 1

print(f"number of anti_freqs: (Part 2) {count}")