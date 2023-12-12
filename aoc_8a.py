def find_path(filepath: str) -> int:
    data = open(filepath, "r").read().split("\n\n")
    dir = data[0]
    print(dir)
    paths = data[1].split("\n")
    path_map = dict()
    for path in paths:
        data = path.split(" = ")
        key = data[0]
        value = data[1][1:len(data[1])-1].split(", ")
        path_map[key] = [value[0], value[1]]
    print(path_map)

    dest = "ZZZ"
    curr = "AAA"
    num_steps = 0
    while curr != dest:
        curr_dir = dir[num_steps%len(dir)]
        if curr_dir == "L":
            curr = path_map.get(curr)[0]
        else:
            curr = path_map.get(curr)[1]
        num_steps += 1
    return num_steps

print(find_path("input/day8.txt"))
