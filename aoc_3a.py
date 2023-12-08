from typing import List


def parts_sum(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]

    sum_part_numbers = 0
    for i in range(len(lines)):
        start = 0
        line = lines[i]
        while start < len(line):
            if line[start].isdigit():
                end = start
                while (end+1) < len(line) and line[end+1].isdigit():
                    end += 1
                if is_neighbor(i, start, end, lines):
                    part_num = int(lines[i][start:end+1])
                    print(part_num)
                    sum_part_numbers += part_num
                start = end + 1
            else:
                start += 1
    return sum_part_numbers


# checks if a number has symbol as neighbor
def is_neighbor(line_idx: int, start_idx: int, end_idx: int, lines: List[str]):
    for row in range(max(0, line_idx-1), min(line_idx+2,len(lines))):
        for col in range(max(0, start_idx-1), min(end_idx+2,len(lines[row]))):
            char = lines[row][col]
            if not char.isdigit() and char != '.':
                return True
    return False


print(parts_sum('input/day3.txt'))

