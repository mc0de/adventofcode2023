from collections import defaultdict


lines = []
x_max = 0
y_max = 0


def has_symbol(x, y):
    global lines
    tl = lines[y-1][x-1] if y > 0 and x > 0 else None
    t = lines[y-1][x] if y > 0 else None
    tr = lines[y-1][x+1] if y > 0 and x < x_max else None
    r = lines[y][x+1] if x < x_max else None
    br = lines[y+1][x+1] if x < x_max and y < y_max else None
    b = lines[y+1][x] if y < y_max else None
    bl = lines[y+1][x-1] if y < y_max and x > 0 else None
    l = lines[y][x-1] if x > 0 else None

    for x in [tl, t, tr, r, br, b, bl, l]:
        if x is not None and x in '=&@+*%/-$#':
            return True
    return False


def part_1():
    global lines, x_max, y_max
    codes = []

    with open('day3/input', 'r') as f:
        lines = [x.strip() for x in f]
        x_max = len(lines[0]) - 1
        y_max = len(lines) - 1

    for y, line in enumerate(lines):
        tmp = ''
        should_count = False
        for x, c in enumerate(line):
            if c.isdigit():
                tmp += c
                if not should_count:
                    should_count = has_symbol(x, y)
            elif should_count:
                codes.append(int(tmp))
                tmp = ''
                should_count = False
            else:
                tmp = ''
                should_count = False

            if (x == x_max or c == '.') and should_count:
                codes.append(int(tmp))
                tmp = ''
                should_count = False

    print(sum(codes))


def has_gear(x, y):
    global lines

    lel = {
        (y-1, x-1): lines[y-1][x-1] if y > 0 and x > 0 else None,
        (y-1, x): lines[y-1][x] if y > 0 else None,
        (y-1, x+1): lines[y-1][x+1] if y > 0 and x < x_max else None,
        (y, x+1): lines[y][x+1] if x < x_max else None,
        (y+1, x+1): lines[y+1][x+1] if x < x_max and y < y_max else None,
        (y+1, x): lines[y+1][x] if y < y_max else None,
        (y+1, x-1): lines[y+1][x-1] if y < y_max and x > 0 else None,
        (y, x-1): lines[y][x-1] if x > 0 else None
    }

    for k, v in lel.items():
        if v is not None and v in '*':
            return k
    return False


def part_2():
    global lines, x_max, y_max

    def def_value():
        return []

    starmap = defaultdict(def_value)

    with open('day3/input', 'r') as f:
        lines = [x.strip() for x in f]
        x_max = len(lines[0]) - 1
        y_max = len(lines) - 1

    for y, line in enumerate(lines):
        tmp = ''
        should_count = False
        for x, c in enumerate(line):
            if c.isdigit():
                tmp += c
                if not should_count:
                    should_count = has_gear(x, y)
            elif should_count:
                starmap[should_count].append(int(tmp))
                tmp = ''
                should_count = False
            else:
                tmp = ''
                should_count = False

            if (x == x_max or c == '.') and should_count:
                starmap[should_count].append(int(tmp))
                tmp = ''
                should_count = False

    print(sum([v[0] * v[1] for k, v in starmap.items() if len(v) == 2]))