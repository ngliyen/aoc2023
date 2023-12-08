def possible_game(game: str, game_num: int) -> int:
    cube_map = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    game_str = game.split(": ")[1]
    game_list = game_str.split("; ")

    for game in game_list:
        results = game.split(", ")
        for result in results:
            breakdown = result.split(" ")
            color = breakdown[1]
            num = int(breakdown[0])
            if num > cube_map[color]:
                return -1
    return game_num


def possible_game_sum(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    total = 0
    for i in range(len(lines)):
        game_score = possible_game(lines[i], i+1)
        if game_score > 0:
            total += game_score
    return total


print(possible_game_sum('input/day2.txt'))