from collections import defaultdict


def part_1():
    game_ids = []
    lim = {'red': 12, 'green': 13, 'blue': 14}

    def def_val():
        return 0

    with open('day2/input', 'r') as f:
        for line in f:
            line = line.split(':')
            game_id = int(line[0].split(' ')[1])
            games = [x.strip() for x in line[1].split(';')]
            colors = defaultdict(def_val)
            for game in games:
                cubes = game.split(',')
                for x in cubes:
                    amount, color = x.strip().split(' ')
                    colors[color] = max(int(amount), colors[color])
            if all([colors['red'] <= lim['red'], colors['green'] <= lim['green'], colors['blue'] <= lim['blue']]):
                game_ids.append(game_id)

    answer = sum(game_ids)
    assert answer == 2369
    print(answer)


def part_2():
    def def_val():
        return 0

    powers = []

    with open('day2/input', 'r') as f:
        for line in f:
            line = line.split(':')
            games = [x.strip() for x in line[1].split(';')]
            colors = defaultdict(def_val)
            for game in games:
                cubes = game.split(',')
                for x in cubes:
                    amount, color = x.strip().split(' ')
                    colors[color] = max(int(amount), colors[color])
            powers.append(colors['red'] * colors['green'] * colors['blue'])

    answer = sum(powers)
    assert answer == 66363
    print(answer)
