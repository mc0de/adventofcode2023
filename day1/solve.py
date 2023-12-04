def part_1():
    with open('day1/input', 'r') as f:
        calibration_codes = []
        for line in f:
            digits = [c for c in line if c in '0123456789']
            calibration_codes.append(int(digits[0] + digits[-1]))
    print(sum(calibration_codes))


def translate(line):
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for k, v in d.items():
        if k in line:
            line = line.replace(k, str(v))
    return line


def find_digit(line, i):
    ll = list(line)
    tmp = ''
    while ll:
        tmp = translate(tmp + ll.pop(i)) if i == 0 else translate(ll.pop(i) + tmp)
        digit = next((c for c in tmp if c.isdigit()), None)
        if digit:
            return digit


def part_2():
    with open('day1/input', 'r') as f:
        calibration_codes = [int(find_digit(line, 0) + find_digit(line, -1)) for line in f]
    print(sum(calibration_codes))
