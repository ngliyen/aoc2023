import collections
from typing import List


def find_min_location(filepath: str) -> (int, int):
    text_blocks = open(filepath, "r").read().split("\n\n")
    seed_ranges = text_blocks[0].split("seeds: ")[1].split(" ")
    seeds = []

    num_ranges = []
    for i in range(1, len(text_blocks)):
        num_range = []
        text = text_blocks[i].split("\n")
        for j in range(len(text)):
            if j > 0:
                num_range.append([int(i) for i in text[j].split(" ")])
        num_ranges.append(num_range)

    for i in range(0, len(seed_ranges), 2):
        seed_range = [int(seed_ranges[i]), int(seed_ranges[i])+int(seed_ranges[i+1])-1]
        seed_boundaries = collections.deque()
        seed_boundaries.append(seed_range)
        for j in range(len(num_ranges)):
            seed_boundaries = find_boundaries(seed_boundaries, num_ranges[j])
        for k in range(len(seed_boundaries)):
            seeds.append(seed_boundaries[k][0])
    return min(seeds)


def find_boundaries(seed_boundaries: collections.deque, num_range: List[List[int]]) -> collections.deque:
    curr_boundaries = seed_boundaries
    next_boundaries = []
    new_boundaries = []
    for i in range(len(num_range)):
        start = num_range[i][1]
        end = num_range[i][1] + num_range[i][2] - 1
        step = num_range[i][0] - start
        for boundary in curr_boundaries:
            curr_start = boundary[0]
            curr_end = boundary[1]
            # out of range
            if curr_end < start or curr_start > end:
                next_boundaries.append(boundary)
            # within the range
            elif curr_start >= start and curr_end <= end:
                new_boundaries.append([curr_start+step, curr_end+step])
                # next_boundaries.append([curr_start, curr_end])
            # middle within range
            elif start > curr_start and end < curr_end:
                next_boundaries.append([curr_start, start-1])
                new_boundaries.append([start+step, end+step])
                # next_boundaries.append([start, end])
                next_boundaries.append([end+1, curr_end])
            # right half within range
            elif start > curr_start and curr_end <= end:
                next_boundaries.append([curr_start, start-1])
                new_boundaries.append([start+step, curr_end+step])
                # next_boundaries.append([start, curr_end])
            # left half within range
            elif start <= curr_start and end < curr_end:
                new_boundaries.append([curr_start+step, end+step])
                # next_boundaries.append([curr_start, end])
                next_boundaries.append([end+1, curr_end])
        curr_boundaries = next_boundaries
        next_boundaries = []
    if len(curr_boundaries) > 0:
        new_boundaries.extend(curr_boundaries)
    return new_boundaries


def find_location(num_ranges: List[List[int]], seed: int) -> int:
    curr_num = seed
    for num_range in num_ranges:
        for i in range(len(num_range)):
            if num_range[i][1] <= curr_num < num_range[i][1] + num_range[i][2]:
                curr_num = num_range[i][0] + (curr_num - num_range[i][1])
                break
    return curr_num


print(find_min_location('input/day5.txt'))

