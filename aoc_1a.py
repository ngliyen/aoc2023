def calibration_sum(filepath: str) -> int:
    with open(filepath) as file:
        lines = [line.rstrip() for line in file]
    total = 0
    for line in lines:
        digit = 0
        first_digit_found = False
        last_digit_found = False
        i = 0
        while not first_digit_found or not last_digit_found:
            if not first_digit_found and line[i].isdigit():
                digit += 10*int(line[i])
                first_digit_found = True
            if not last_digit_found and line[-i-1].isdigit():
                digit += int(line[-i-1])
                last_digit_found = True
            i += 1
        total += digit
        print(digit)
    return total


print(calibration_sum('input/day1.txt'))


