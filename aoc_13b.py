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
        num_off = 0
        while mid - offset + 1 >= 0 and mid + offset < len(puzzle):
            for col in range(len(puzzle[0])):
                if puzzle[mid-offset + 1][col] != puzzle[mid+offset][col]:
                    num_off += 1
            offset += 1
        if num_off == 1:
            return mid+1
    return 0


def find_col_reflection(puzzle: List[str]) -> int:
    for i in range(len(puzzle[0])-1):
        mid = i
        offset = 1
        num_off = 0
        while mid - offset + 1 >= 0 and mid + offset < len(puzzle[0]):
            for row in range(len(puzzle)):
                left = puzzle[row][mid-offset+1]
                right = puzzle[row][mid+offset]
                if left != right:
                    num_off += 1
            offset += 1
        if num_off == 1:
            return mid + 1
    return 0

print(find_reflection("input/day13.txt"))

