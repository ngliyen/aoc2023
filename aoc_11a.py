from typing import List

def shortest_path(filepath: str) -> int:
    grid = expand_grid(filepath)
    loc = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                loc.append((row, col))
    print(loc)

    total = 0
    count = 0
    for i in range(len(loc)):
        for j in range(i+1, len(loc)):
            path = abs(loc[i][0]-loc[j][0]) + abs(loc[i][1]-loc[j][1])
            total += path
            count += 1

    return total



def expand_grid(filepath: str) -> List[List[str]]:
    grid = []
    lines = open(filepath, "r").read().split("\n")
    # expand row
    for row in range(len(lines)):
        all_dot = True
        curr_line = []
        for col in range(len(lines[row])):
            curr_line.append(lines[row][col])
            if lines[row][col] != ".":
                all_dot = False
        grid.append(curr_line)
        if all_dot:
            grid.append(curr_line.copy())

    # expand col
    shift_col = 0
    col = 0
    while col < len(grid[0]):
        all_dot = True
        for row in range(len(grid)):
            if grid[row][col] != ".":
                all_dot = False
        if all_dot:
            for row in range(len(grid)):
                grid[row].insert(col+1, ".")
            col += 1
        col += 1

    return grid

print(shortest_path("input/day11_test.txt"))
print(shortest_path("input/day11.txt"))
