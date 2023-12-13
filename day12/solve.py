from itertools import permutations, combinations, combinations_with_replacement


def part_1():
    records = [x.strip() for x in open('day12/input', 'r') if x != '\n']

    answer = 0
    for record in records:
        pattern, log = record.split()
        shapes = list(map(int, log.split(',')))
        gaps = len(shapes) - 1
        free_spaces = len(pattern) - (sum(shapes) + gaps)
        # print(pattern, shapes, gaps, free_spaces)
        configs = gap_configuration(free_spaces, gaps + 2)

        arrangements = [draw_shape(x, shapes) for x in configs]
        matches = filter_pattern(pattern, arrangements)
        # print(matches)
        # print(len(matches))
        answer += len(matches)

    assert answer == 7653
    print(answer)


def filter_pattern(pattern, arrangements):
    for i, c in enumerate(pattern):
        if c in '#.':
            arrangements = [x for x in arrangements if x[i] == c]
    return arrangements


def draw_shape(config, shapes):
    shapes = shapes[:]
    shapes.append(0)
    s = ''

    for i, x in enumerate(config):
        s += '.' * x
        s += '#' * shapes.pop(0)
    return s


def gap_configuration(stones, holes):
    c = combinations([x for x in range(stones + 1)] * holes, holes)
    f = set(f for f in c if sum(f) == stones)
    r = []
    for t in f:
        segment = []
        for i, x in enumerate(t):
            if 0 < i < holes - 1:
                x += 1
            segment.append(x)
        r.append(tuple(segment))
    return r


def part_2():
    records = [x.strip() for x in open('day12/input2', 'r') if x != '\n']

    answer = 0
    pattern, log = records[1].split()
    pattern = '?'.join([pattern] * 5)
    log = ','.join([log] * 5)

    shapes = list(map(int, log.split(',')))
    gaps = len(shapes) - 1
    free_spaces = len(pattern) - (sum(shapes) + gaps)
    print(pattern, shapes, gaps, free_spaces)
    configs = gap_configuration(free_spaces, gaps + 2)

    arrangements = [draw_shape(x, shapes) for x in configs]
    matches = filter_pattern(pattern, arrangements)
    print(matches)
    print(len(matches))
    answer += len(matches)
