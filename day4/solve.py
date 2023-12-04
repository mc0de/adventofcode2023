import re
from collections import defaultdict


def part_1():
    scores = []

    with open('day4/input', 'r') as f:
        for line in f:
            score = 0
            c, numbers = line.split(':')
            winning, have = numbers.split('|')
            winning = re.sub(r'\s+', ' ', winning).split()
            have = re.sub(r'\s+', ' ', have).split()
            for x in winning:
                if x in have:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2
            scores.append(score)

    print(sum(scores))


def search(q, lines):
    for i, x in enumerate(lines):
        if x.startswith(q):
            return i


def part_2():
    mm = []

    def def_val():
        return 1

    with open('day4/input', 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    repeater = defaultdict(def_val)

    for line in lines:
        c, numbers = line.split(':')
        card = int(c.split()[1])
        winning, have = numbers.split('|')
        winning = re.sub(r'\s+', ' ', winning).split()
        have = re.sub(r'\s+', ' ', have).split()

        matches = 0
        for x in winning:
            if x in have:
                matches += 1

        for x in range(1, min(matches + 1, len(lines))):
            repeater[card + x] += repeater[card]
        mm.append(repeater[card])

    print(sum(mm))