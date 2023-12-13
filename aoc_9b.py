from typing import List


def next_num(filepath: str) -> int:
    puzzles = open(filepath, "r").read().split("\n")

    total = 0
    for p in puzzles:
        puzzle = [int(i) for i in p.split(" ")]
        total += extrapolate(puzzle)
    return total

def extrapolate(puzzle: List[int]) -> int:
    data = [puzzle]
    is_last_row = False
    curr_row = puzzle
    while not is_last_row:
        is_last_row = True
        next_row = []
        for i in range(len(curr_row)-1):
            diff = curr_row[i+1] - curr_row[i]
            next_row.append(diff)
            if diff != 0:
                is_last_row = False
        if not is_last_row:
            data.append(next_row)
            curr_row = next_row

    num = 0
    for i in range(len(data)):
        row = -i-1
        num = data[row][0] - num
    print(num)
    return num

print(next_num("input/day9.txt"))

