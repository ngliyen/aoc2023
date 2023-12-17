from typing import List


def pipe_distance(filepath: str) -> int:
    pipe_map = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": []
    }

    pipes = []
    lines = open(filepath, "r").read().split("\n")
    for line in lines:
        pipes.append([*line])
    start_found = False
    for row in range(len(pipes)):
        for col in range(len(pipes[0])):
            if pipes[row][col] == "S":
                start = (row, col)
                start_found = True
                break
        if start_found:
            break

    find_start_pipe(pipes, pipe_map, start)

    loop_found = False
    (curr_row, curr_col) = (start[0], start[1])
    grid = [[0]*len(pipes[0]) for i in range(len(pipes))]
    grid[curr_row][curr_col] = 1

    count = 1
    curr_dir = pipe_map.get(pipes[curr_row][curr_col])[0]
    while not loop_found:
        (curr_row, curr_col) = (curr_row+curr_dir[0], curr_col+curr_dir[1])
        grid[curr_row][curr_col] = 1
        if (curr_row, curr_col) == start:
            loop_found = True
            break
        pipe = pipes[curr_row][curr_col]
        for dr in pipe_map.get(pipe):
            if not (dr[0]+curr_dir[0] == 0 and dr[1]+curr_dir[1] == 0):
                curr_dir = dr
                break
        count += 1
    # if loop_found:
    #     for line in grid:
    #         print(line)

    new_grid = expand_grid(pipes, grid)
    # for line in new_grid:
    #     print(line)

    not_enclosed_count = find_not_enclosed(new_grid)
    total_nodes = len(pipes[0])*len(pipes)
    print("Pipe count: ", count)
    print("Not enclosed: ", not_enclosed_count)
    print("Total: ", total_nodes)
    return total_nodes - not_enclosed_count - count


def find_start_pipe(pipes, pipe_map, start) -> None:
    # find the start pipe type
    for p in pipe_map.keys():
        directions = pipe_map.get(p)
        # for each direction in curr_dir, we need to make sure it connects to start
        for curr_dir in directions:
            neighbor = (start[0] + curr_dir[0], start[1] + curr_dir[1])
            neighbor_dir = pipe_map.get(pipes[neighbor[0]][neighbor[1]])
            pipe_type_found = False
            for nd in neighbor_dir:
                if (neighbor[0] + nd[0], neighbor[1] + nd[1]) == start:
                    pipe_type_found = True
                    break
            if not pipe_type_found:
                break
        if pipe_type_found:
            print(p)
            pipes[start[0]][start[1]] = p
            break


def expand_grid(pipes: List[List[str]], path: List[List[int]]) -> List[List[int]]:
    pipe_map = {
        "|": [[0,1,0],[0,1,0],[0,1,0]],
        "-": [[0,0,0],[1,1,1],[0,0,0]],
        "L": [[0,1,0],[0,1,1],[0,0,0]],
        "J": [[0,1,0],[1,1,0],[0,0,0]],
        "7": [[0,0,0],[1,1,0],[0,1,0]],
        "F": [[0,0,0],[0,1,1],[0,1,0]],
        ".": [[0,0,0],[0,0,0],[0,0,0]]
    }

    new_grid = []
    zero_row = [0]*(3*len(pipes[0])+2)

    new_grid.append(zero_row)
    for row in range(len(pipes)):
        sub_row_1 = [0]
        sub_row_2 = [0]
        sub_row_3 = [0]
        for col in range(len(pipes[row])):
            if path[row][col] == 1:
                pipe_setup = pipe_map.get(pipes[row][col])
                sub_row_1.extend(pipe_setup[0])
                sub_row_2.extend(pipe_setup[1])
                sub_row_3.extend(pipe_setup[2])
            else:
                sub_row_1.extend([0]*3)
                sub_row_2.extend([0]*3)
                sub_row_3.extend([0]*3)
        sub_row_1.append(0)
        sub_row_2.append(0)
        sub_row_3.append(0)
        new_grid.append(sub_row_1)
        new_grid.append(sub_row_2)
        new_grid.append(sub_row_3)

    return new_grid


def find_not_enclosed(grid: List[List[int]]) -> int:
    not_enclosed_count = 0
    neighbor_dir = [[-1,0],[0,-1],[0,1],[1,0]]
    curr_nodes = [[0, 0]]
    visited = [[False]*len(grid[0]) for i in range(len(grid))]
    visited[0][0] = True
    while len(curr_nodes) != 0:
        next_nodes = []
        for node in curr_nodes:
            curr_row = node[0]
            curr_col = node[1]
            if curr_row % 3 == 1 and curr_col % 3 == 1 and is_empty_node(curr_row, curr_col, grid):
                not_enclosed_count += 1
            for d in neighbor_dir:
                row = node[0] + d[0]
                col = node[1] + d[1]
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 1 and not visited[row][col]:
                    visited[row][col] = True
                    next_nodes.append([row,col])
        curr_nodes = next_nodes
    return not_enclosed_count


def is_empty_node(row: int, col: int, grid: List[List[int]]) -> bool:
    for i in range(3):
        for j in range(3):
            if row+i >= len(grid) or col+j >= len(grid[row]) or grid[row+i][col+j] != 0:
                return False
    # print("Empty:", row//3, col//3)
    return True





print(pipe_distance("input/day10.txt"))

