from collections import namedtuple
from itertools import combinations

Coordinate = namedtuple('pos', ['x', 'y'])


def part_1():
    space = [x.strip() for x in open('day11/input', 'r') if x != '\n']
    space = expand_xy(space)
    galaxies = []

    for y, line in enumerate(space):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append(Coordinate(x, y))

    pairs = list(combinations(galaxies, 2))

    answer = 0
    for a, b in pairs:
        answer += abs(a.x - b.x) + abs(a.y - b.y)

    assert answer == 9545480
    print(answer)


def expand_xy(space):
    return transform(expand(transform(expand(space))))


def expand(space):
    expanded = []
    for row in space:
        if '#' not in row:
            expanded.append(row)
        expanded.append(row)
    return expanded


def transform(space):
    transformed = []
    for x in range(len(space[0])):
        col = ''
        for y in range(len(space)):
            col += space[y][x]
        transformed.append(col)
    return transformed


def wormholes(space):
    e = []
    for y, line in enumerate(space):
        if '#' not in line:
            e.append(y)
    return e


def part_2():
    scale = 1000000

    space = [x.strip() for x in open('day11/input', 'r') if x != '\n']
    empty_xs = wormholes(space)
    empty_ys = wormholes(transform(space))
    galaxies = []

    for y, line in enumerate(space):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append(Coordinate(x, y))

    pairs = list(combinations(galaxies, 2))

    answer = 0
    for a, b in pairs:
        distance = abs(a.x - b.x) + abs(a.y - b.y)

        if a.x < b.x:
            for s in empty_ys:
                if s in range(a.x + 1, b.x):
                    distance += scale - 1
        if b.x < a.x:
            for s in empty_ys:
                if s in range(b.x + 1, a.x):
                    distance += scale - 1
        if a.y < b.y:
            for s in empty_xs:
                if s in range(a.y + 1, b.y):
                    distance += scale - 1
        if b.y < a.y:
            for s in empty_xs:
                if s in range(b.y + 1, a.y):
                    distance += scale - 1
        answer += distance

    assert answer == 406725732046
    print(answer)
