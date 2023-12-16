from typing import List

def shortest_path(mult: int, empty_rows: List[int], empty_cols: List[int], locations: List[List[int]], total_rows: int, total_cols: int) -> int:
    for loc in locations:
        row = loc[0]
        for i in range(len(empty_rows)):
            if i == 0 and row <= empty_rows[0]:
                shift_row = 0
                break
            elif i < len(empty_rows) and empty_rows[i-1] < row <= empty_rows[i]:
                shift_row = i
                break
            elif i == len(empty_rows) - 1 and row > empty_rows[i]:
                shift_row = i + 1
                break
        loc[0] = row + shift_row*(mult-1)

    for loc in locations:
        col = loc[1]
        for i in range(len(empty_cols)):
            if i == 0 and col <= empty_cols[0]:
                shift_col = 0
                break
            elif i < len(empty_cols) and empty_cols[i-1] < col <= empty_cols[i]:
                shift_col = i
                break
            elif i == len(empty_cols) - 1 and col > empty_cols[i]:
                shift_col = i + 1
                break
        loc[1] = col + shift_col*(mult-1)
    print(locations)

    total = 0
    count = 0
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            path = abs(locations[i][0]-locations[j][0]) + abs(locations[i][1]-locations[j][1])
            total += path
            count += 1

    print(count)
    return total

def expand_grid(filepath: str) -> List[List[str]]:
    loc = []
    empty_rows = []
    empty_cols = []
    lines = open(filepath, "r").read().split("\n")
    # expand row
    for row in range(len(lines)):
        all_dot = True
        for col in range(len(lines[row])):
            if lines[row][col] != ".":
                all_dot = False
                loc.append([row,col])
        if all_dot:
            empty_rows.append(row)

    # expand col
    for col in range(len(lines[0])):
        all_dot = True
        for row in range(len(lines)):
            if lines[row][col] != ".":
                all_dot = False
                break
        if all_dot:
            empty_cols.append(col)

    print(empty_rows)
    print(empty_cols)
    print(loc)
    return shortest_path(1000000, empty_rows, empty_cols, loc, len(lines), len(lines[0]))
print(expand_grid("input/day11.txt"))

# [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
