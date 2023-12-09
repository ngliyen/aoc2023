import collections
from typing import List


def points_won(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]

    points = 0
    match_list = [0]*len(lines)
    for i in range(len(lines)):
        numbers = lines[i].split(": ")[1].split(" | ")
        winning_nums = numbers[0].split()
        nums_owned = numbers[1].split()
        matches = number_of_match(winning_nums, nums_owned)
        if matches > 0:
            match_list[i] = matches

    return number_of_cards(match_list)


def number_of_cards(match_list: List[int]) -> int:
    total_cards = 0
    card_sequence = collections.deque()
    for i in range(len(match_list)):
        card_sequence.append(i)
    while len(card_sequence) > 0:
        curr = card_sequence.popleft()
        total_cards += 1
        for j in range(1, match_list[curr]+1):
            card_sequence.append(curr+j)
    return total_cards

def number_of_match(winning_nums: List[int], nums_owned: List[int]) -> int:
    winning_nums.sort()
    nums_owned.sort()
    match = 0
    win_idx = 0
    start = 0
    end = len(nums_owned)-1
    while start < len(nums_owned) and win_idx < len(winning_nums):
        idx = search(start, end, winning_nums[win_idx], nums_owned)
        if idx >= 0:
            match += 1
            start = idx + 1
        win_idx += 1
    return match


def search(start: int, end: int, target: int, nums: List[int]) -> int:
    mid = (start+end)//2

    if start > end:
        return -1
    elif nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return search(mid+1, end, target, nums)
    else:
        return search(start, mid-1, target, nums)

print(points_won('input/day4.txt'))