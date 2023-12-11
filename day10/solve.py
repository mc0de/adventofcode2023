from collections import namedtuple


maze = []
Coordinate = namedtuple('pos', ['x', 'y'])


def part_1():
    global maze
    maze = [x.strip() for x in open('day10/input', 'r') if x != '\n']

    start_pos = find_s(maze)
    connections = find_conns(start_pos)
    replace_s_to_pipe(start_pos, connections)

    pos, direction, steps = start_pos, connections[0], 1
    while True:
        pos, direction = go(pos, direction)
        if pos == start_pos:
            break
        steps += 1

    answer = steps // 2
    assert answer == 6903
    print(answer)


def find_s(rows):
    for y, line in enumerate(rows):
        x = line.find('S')
        if x != -1:
            return Coordinate(x, y)


def find_conns(start):
    e = ''
    for direction in ['N', 'S', 'E', 'W']:
        new_pos, new_dir = go(start, direction)
        if new_dir is not None:
            e += direction
    return e


def replace_s_to_pipe(start_pos, connections):
    global maze
    pipes = {'NS': '|', 'NE': 'L', 'NW': 'J', 'SE': 'F', 'SW': '7', 'EW': '-'}
    line = list(maze[start_pos.y])
    line[start_pos.x] = pipes[connections]
    maze[start_pos.y] = ''.join(line)


def go(coord, direction):
    next_node = {
        'N': Coordinate(coord.x, coord.y - 1),
        'S': Coordinate(coord.x, coord.y + 1),
        'E': Coordinate(coord.x + 1, coord.y),
        'W': Coordinate(coord.x - 1, coord.y),
    }
    pipe_from_to = {
        '|': {'N': 'S', 'S': 'N', 'W': None, 'E': None},
        '-': {'E': 'W', 'W': 'E', 'S': None, 'N': None},
        'L': {'N': 'E', 'E': 'N', 'W': None, 'S': None},
        'J': {'N': 'W', 'W': 'N', 'S': None, 'E': None},
        '7': {'S': 'W', 'W': 'S', 'N': None, 'E': None},
        'F': {'S': 'E', 'E': 'S', 'N': None, 'W': None},
        '.': {'N': None, 'S': None, 'E': None, 'W': None},
    }
    from_to = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    new_coord = next_node[direction]
    new_poi = poi(new_coord)
    new_direction = pipe_from_to[new_poi][from_to[direction]]
    return new_coord, new_direction


def poi(coord):
    global maze
    return maze[coord.y][coord.x]


def part_2():
    global maze
    maze = [x.strip() for x in open('day10/input', 'r') if x != '\n']

    start_pos = find_s(maze)
    connections = find_conns(start_pos)
    replace_s_to_pipe(start_pos, connections)

    pos, direction, = start_pos, connections[0]
    path = []
    while True:
        path.append(pos)
        pos, direction = go(pos, direction)
        if pos == start_pos:
            break
    path_set = set(path)

    xs = [pos.x for pos in path_set]
    ys = [pos.y for pos in path_set]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

    sliced = []
    dots = []
    for new_y, y in enumerate(range(min_y, max_y + 1)):
        line = ''
        for new_x, x in enumerate(range(min_x, max_x + 1)):
            coord = Coordinate(x, y)
            if coord not in path_set:
                line += '.'
                dots.append(Coordinate(new_x, new_y))
            else:
                line += poi(coord)
        sliced.append(line)

    answer = 0
    for dot in dots:
        inside = False
        waiting = None
        for c in sliced[dot.y][:dot.x]:
            if c == '|':
                inside = not inside
            elif c == 'L':
                waiting = '7'
            elif c == 'F':
                waiting = 'J'
            elif c == waiting:
                inside = not inside
        if inside:
            answer += 1
    assert answer == 265
    print(answer)
