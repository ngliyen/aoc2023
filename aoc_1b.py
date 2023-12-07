def replace_num_str_with_num(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]

    total = 0
    for line in lines:
        curr = 10*find_first_digit(line) + find_last_digit(line)
        print(curr)
        total += curr
    return total


def find_first_digit(s: str) -> int:
    num_str_map = {
        "o": [("one", 1)],
        "t": [("two", 2), ("three", 3)],
        "f": [("four", 4), ("five", 5)],
        "s": [("six", 6), ("seven", 7)],
        "e": [("eight", 8)],
        "n": [("nine", 9)]
    }
    i = 0
    first_digit_found = False
    while not first_digit_found and i < len(s):
        if s[i].isdigit():
            return int(s[i])
        elif num_str_map.get(s[i]) is not None:
            potential_digits = num_str_map[s[i]]
            for digit in potential_digits:
                first_digit_found = True
                for j in range(len(digit[0])):
                    if i+j >= len(s) or s[i+j] != digit[0][j]:
                        first_digit_found = False
                        break
                if first_digit_found:
                    return digit[1]
        i += 1
    return 0


def find_last_digit(s: str) -> int:
    num_str_map = {
        "e": [("eno", 1), ("eerht", 3), ("evif", 5), ("enin", 9)],
        "o": [("owt", 2)],
        "r": [("ruof", 4), ],
        "x": [("xis", 6), ],
        "t": [("thgie", 8)],
        "n": [("neves", 7)]
    }

    i = len(s)-1
    last_digit_found = False
    while not last_digit_found and i >= 0:
        if s[i].isdigit():
            return int(s[i])
        elif num_str_map.get(s[i]) is not None:
            potential_digits = num_str_map[s[i]]
            for digit in potential_digits:
                last_digit_found = True
                for j in range(len(digit[0])):
                    if i-j < 0 or s[i-j] != digit[0][j]:
                        last_digit_found = False
                        break
                if last_digit_found:
                    return digit[1]
        i -= 1
    return 0


print(replace_num_str_with_num('input/day1.txt'))

#53985
#54100
