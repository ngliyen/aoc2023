from typing import List


def nearest_location(filepath: str) -> int:
    text_blocks = open(filepath, "r").read().split("\n\n")
    seeds = text_blocks[0].split("seeds: ")[1].split(" ")
    num_ranges = []
    for i in range(1, len(text_blocks)):
        num_range = []
        text = text_blocks[i].split("\n")
        for j in range(len(text)):
            if j > 0:
                num_range.append([int(i) for i in text[j].split(" ")])
        num_ranges.append(num_range)
    print(num_ranges)

    location = find_location(num_ranges, int(seeds[0]))
    for seed in seeds:
        location = min(find_location(num_ranges, int(seed)), location)
    return location


def find_location(num_ranges: List[List[int]], seed: int) -> int:
    curr_num = seed
    for num_range in num_ranges:
        for i in range(len(num_range)):
            if num_range[i][1] <= curr_num < num_range[i][1] + num_range[i][2]:
                curr_num = num_range[i][0] + (curr_num - num_range[i][1])
                break
    return curr_num

print(nearest_location("input/day5.txt"))
