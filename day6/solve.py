import re


def part_1():
    lines = [re.sub(r'\s+', ' ', x.strip()) for x in open('day6/input', 'r')]
    times = [int(x) for x in lines[0].split()[1:]]
    records = [int(x) for x in lines[1].split()[1:]]
    races = list(zip(times, records))
    score = 1

    for time, record in races:
        ways = 0
        for x in range(time + 1):
            distance = x * (time - x)
            if distance > record:
                ways += 1
        score *= ways
    print(score)


def part_2():
    lines = [re.sub(r'\s+', ' ', x.strip()) for x in open('day6/input', 'r')]
    time = int(''.join(lines[0].split()[1:]))
    record = int(''.join(lines[1].split()[1:]))
    ways = 0

    for x in range(time + 1):
        distance = x * (time - x)
        if distance > record:
            ways += 1
    print(ways)
