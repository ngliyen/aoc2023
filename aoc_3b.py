from typing import List


def gear_ratio_sum(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    gear_sum = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "*":
                gear_sum += gear_ratio(row, col, lines)
    return gear_sum


# checks if a number has symbol as neighbor
def gear_ratio(line_idx: int, gear_col: int, lines: List[str]) -> int:
    visited = []
    nums = []
    for row in range(max(0, line_idx-1), min(line_idx+2,len(lines))):
        for col in range(max(0, gear_col-1), min(gear_col+2,len(lines[row]))):
            visit_str = "r" + str(row) + "c" + str(col)
            if visit_str in visited:
                next
            else:
                visited.append(visit_str)
                char = lines[row][col]
                if char.isdigit():
                    num = find_num(row, col, lines[row], visited)
                    nums.append(num)
    if len(nums) == 2:
        print(nums)
        return nums[0]*nums[1]
    else:
        return 0


def find_num(row_idx: int, curr_idx: int, line: str, visited: List[str]) -> int:
    # find start of string
    start_found = False
    start_idx = curr_idx
    while not start_found and start_idx > 0:
        visited.append("r"+str(row_idx)+"c"+str(start_idx-1))
        if line[start_idx-1].isdigit():
            start_idx -= 1
        else:
            start_found = True
    # find end of string
    end_found = False
    end_idx = curr_idx
    while not end_found and end_idx < len(line) - 1:
        visited.append("r"+str(row_idx)+"c"+str(end_idx+1))
        if line[end_idx+1].isdigit():
            end_idx += 1
        else:
            end_found = True
    return int(line[start_idx: end_idx+1])


print(gear_ratio_sum(('input/day3.txt')))

