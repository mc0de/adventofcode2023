from math import gcd
from functools import reduce
from itertools import count, cycle


def part_1():
    lines = [x.strip() for x in open('day8/input', 'r') if x != '\n']

    path, network, next_node = lines[0], parse_network(lines[1:]), 'AAA'

    for steps, x in navigate(path):
        next_node = network[next_node][x]
        if next_node == 'ZZZ':
            assert steps == 19631
            print(steps)
            return


def parse_network(lines):
    translation_table = str.maketrans({'=': '', '(': '', ')': '', ',': ''})
    return {node: {'L': pl, 'R': pr} for node, pl, pr in (x.translate(translation_table).split() for x in lines)}


def navigate(path):
    for i, x in zip(count(start=1), cycle(path)):
        yield i, x


def part_2():
    lines = [x.strip() for x in open('day8/input', 'r') if x != '\n']

    path, network = lines[0], parse_network(lines[1:])
    entry_nodes, skip_nodes, intervals = [node for node in network if node.endswith('A')], [], []

    for steps, x in navigate(path):
        for i, node in enumerate(entry_nodes):
            if i not in skip_nodes:
                entry_nodes[i] = network[node][x]
                if entry_nodes[i][-1] == 'Z':
                    skip_nodes.append(i)
                    intervals.append(steps)
        if len(skip_nodes) == len(entry_nodes):
            break

    answer = reduce(lambda x, y: x * y // gcd(x, y), intervals, 1)
    assert answer == 21003205388413
    print(answer)
