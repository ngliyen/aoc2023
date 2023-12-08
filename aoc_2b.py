def game_power(game: str) -> int:
    cube_map = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game_str = game.split(": ")[1]
    game_list = game_str.split("; ")

    for game in game_list:
        rounds = game.split(", ")
        for round in rounds:
            result = round.split(" ")
            color = result[1]
            num = int(result[0])
            if num > cube_map[color]:
                cube_map[color] = num
    return cube_map["red"]*cube_map["green"]*cube_map["blue"]


def possible_game_sum(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    total = 0
    for i in range(len(lines)):
        power = game_power(lines[i])
        total += power
    return total


print(possible_game_sum('input/day2.txt'))