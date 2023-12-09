from itertools import accumulate


def part_1():
    histories = [x.strip().split() for x in open('day9/input', 'r') if x != '\n']
    total = 0
    for entry in histories:
        tree = mk_tree(entry)
        total += [x for x in accumulate([x[-1] for x in tree])][-1]

    assert total == 1708206096
    print(total)


def mk_tree(entry):
    entry = [int(x) for x in entry]
    tree = [entry]
    while any(entry):
        entry = [y - x for x, y in zip(entry, entry[1:])]
        tree.append(entry)
    return tree[::-1]


def part_2():
    histories = [x.strip().split() for x in open('day9/input', 'r') if x != '\n']
    total = 0
    for entry in histories:
        tree = mk_tree(entry)
        total += [x for x in accumulate([x[0] for x in tree], lambda x, y: y - x)][-1]

    assert total == 1050
    print(total)
