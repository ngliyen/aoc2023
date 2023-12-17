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
    print(pipes)
    start_found = False
    for row in range(len(pipes)):
        for col in range(len(pipes[0])):
            if pipes[row][col] == "S":
                start = (row, col)
                start_found = True
                break
        if start_found:
            break


    loop_found = False
    for p in pipe_map.keys():
        print("Start", p)
        p1 = start
        pipes[p1[0]][p1[1]] = p
        visited = [[0]*len(pipes[0]) for i in range(len(pipes))]
        visited[start[0]][start[1]] = True
        connected = True
        count = 0
        while connected and not loop_found:
            pipe = pipes[p1[0]][p1[1]]
            connected = False
            for direction in pipe_map.get(pipe):
                p2 = (p1[0]+direction[0], p1[1]+direction[1])
                if p2 == start and count > 1:
                    loop_found = True
                    break
                if not visited[p2[0]][p2[1]]:
                    if is_connected(p1, p2, pipes):
                        visited[p2[0]][p2[1]] = True
                        count += 1
                        connected = True
                        p1 = p2
                        break
        print(pipes[start[0]][start[1]])
        if loop_found:
            print(p)
            return count//2 + count%2
    return -1


def is_connected(p1: (int, int), p2: (int, int), pipes: List[str]) -> bool:
    pipe_map = {
        "|": [(-1, 0), (1, 0)],
        "-": [(0, -1), (0, 1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(0, -1), (1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": []
    }

    p1_shape = pipes[p1[0]][p1[1]]
    p2_shape = pipes[p2[0]][p2[1]]

    if p1_shape == "." or p2_shape == ".":
        return False

    p2_is_neighbor = get_neighbors(p1[0], p1[1], pipe_map.get(p1_shape), p2[0], p2[1])
    p1_is_neighbor = get_neighbors(p2[0], p2[1], pipe_map.get(p2_shape), p1[0], p1[1])

    if p1_is_neighbor and p2_is_neighbor:
        return True


def get_neighbors(row: int, col: int, directions: List[tuple], row2: int, col2: int) -> bool:
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if new_row == row2 and new_col == col2:
            return True
    return False

print(pipe_distance("input/day10.txt"))

