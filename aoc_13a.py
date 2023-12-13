from typing import List


def find_reflection(filepath: str) -> int:
    puzzles = open(filepath, "r").read().split("\n\n")
    total = 0
    for p in puzzles:
        puzzle = p.split("\n")
        row = find_row_reflection(puzzle)
        col = find_col_reflection(puzzle)
        print(puzzle, row, col)
        total += row*100 + col
    return total


def find_row_reflection(puzzle: List[str]) -> int:
    for i in range(len(puzzle)-1):
        mid = i
        offset = 1
        line_found = True
        while mid - offset + 1 >= 0 and mid + offset < len(puzzle):
            if puzzle[mid-offset + 1] != puzzle[mid+offset]:
                line_found = False
            offset += 1
        if line_found:
            return mid+1
    return 0


def find_col_reflection(puzzle: List[str]) -> int:
    for i in range(len(puzzle[0])-1):
        mid = i
        offset = 1
        line_found = True
        while mid - offset + 1 >= 0 and mid + offset < len(puzzle[0]):
            for row in range(len(puzzle)):
                left = puzzle[row][mid-offset+1]
                right = puzzle[row][mid+offset]
                if left != right:
                    line_found = False
                    break
            if not line_found:
                break
            offset += 1
        if line_found:
            return mid + 1
    return 0

print(find_reflection("input/day13.txt"))

