from typing import List


def find_path(filepath: str) -> int:
    data = open(filepath, "r").read().split("\n\n")
    dir = data[0]
    paths = data[1].split("\n")
    path_map = dict()
    for path in paths:
        data = path.split(" = ")
        key = data[0]
        value = data[1][1:len(data[1])-1].split(", ")
        path_map[key] = [value[0], value[1]]

    curr_locations = []
    for loc in path_map.keys():
        if loc[-1] == "A":
            curr_locations.append(loc)
    print(curr_locations)
    num_steps = 0
    z_location = [-1]*len(curr_locations)
    loc_found = 0
    while loc_found != len(curr_locations):
        next_locations = []
        for i in range(len(curr_locations)):
            dir_idx = num_steps%len(dir)
            next_location = find_next(curr_locations[i], path_map, num_steps, dir[dir_idx])
            next_locations.append(next_location)
            if next_location[-1] == "Z" and z_location[i] == -1:
                z_location[i] = num_steps + 1
                loc_found += 1
                print(num_steps, i, next_location)
        curr_locations = next_locations
        num_steps += 1
    return lcm(z_location)


def find_next(curr: str, path_map: dict(), num_steps: int, curr_dir: str) -> str:
    if curr_dir == "L":
        curr = path_map.get(curr)[0]
    else:
        curr = path_map.get(curr)[1]
    return curr

def all_z_locations(locations: List[str]) -> bool:
    for loc in locations:
        if loc[-1] != "Z":
            return False
    return True


def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(nums: List[int]) -> int:
    lcm = 1
    for i in nums:
        lcm = (lcm*i) // gcd(lcm,i)
    return lcm

print(lcm)
# print(lcm([1,2,5]))
print(find_path("input/day8.txt"))
