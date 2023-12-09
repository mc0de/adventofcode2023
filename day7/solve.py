from collections import Counter


def part_1():
    d = {
        'five': [],
        'four': [],
        'house': [],
        'three': [],
        'pairs': [],
        'pair': [],
        'high': []
    }

    lines = [x.strip().split(' ') for x in open('day7/input', 'r') if x != '\n']
    table = str.maketrans({'A': 'T', 'T': 'A', 'K': 'Q', 'Q': 'K'})

    for hand, bid in lines:
        hand = hand.translate(table)
        bid = int(bid)
        cc = list(Counter(hand).values())
        cc.sort(reverse=True)
        if cc == [5]:
            d['five'].append((hand, bid))
            continue

        if cc == [4, 1]:
            d['four'].append((hand, bid))
            continue

        if cc == [3, 2]:
            d['house'].append((hand, bid))
            continue

        if cc == [3, 1, 1]:
            d['three'].append((hand, bid))
            continue

        if cc == [2, 2, 1]:
            d['pairs'].append((hand, bid))
            continue

        if cc == [2, 1, 1, 1]:
            d['pair'].append((hand, bid))
            continue

        d['high'].append((hand, bid))

    stack = []
    for t, l in d.items():
        l.sort(reverse=True)
        stack.extend(l)

    score = 0
    ll = len(stack)
    for x in stack:
        score += x[1] * ll
        ll -= 1

    assert score == 248422077
    print(score)


def part_2():
    d = {
        'five': [],
        'four': [],
        'house': [],
        'three': [],
        'pairs': [],
        'pair': [],
        'high': []
    }

    lines = [x.strip().split(' ') for x in open('day7/input', 'r') if x != '\n']
    table = str.maketrans({'A': 'T', 'T': 'A', 'K': 'Q', 'Q': 'K', 'J': '1'})

    for hand, bid in lines:
        hand = hand.translate(table)
        bid = int(bid)
        cc = list(Counter(hand).values())
        cc.sort(reverse=True)
        if '1' in hand:
            if cc == [5]:
                d['five'].append((hand, bid))
                continue
            if cc == [4, 1]:
                d['five'].append((hand, bid))
                continue
            if cc == [3, 2]:
                d['five'].append((hand, bid))
                continue
            if cc == [3, 1, 1]:
                d['four'].append((hand, bid))
                continue
            if cc == [2, 2, 1]:
                cc = Counter(hand)
                if cc['1'] == 1:
                    d['house'].append((hand, bid))
                else:
                    d['four'].append((hand, bid))
                continue
            if cc == [2, 1, 1, 1]:
                d['three'].append((hand, bid))
                continue
            d['pair'].append((hand, bid))
        else:
            if cc == [5]:
                d['five'].append((hand, bid))
                continue

            if cc == [4, 1]:
                d['four'].append((hand, bid))
                continue

            if cc == [3, 2]:
                d['house'].append((hand, bid))
                continue

            if cc == [3, 1, 1]:
                d['three'].append((hand, bid))
                continue

            if cc == [2, 2, 1]:
                d['pairs'].append((hand, bid))
                continue

            if cc == [2, 1, 1, 1]:
                d['pair'].append((hand, bid))
                continue

            d['high'].append((hand, bid))

    stack = []
    for t, l in d.items():
        l.sort(reverse=True)
        stack.extend(l)

    score = 0
    ll = len(stack)
    for x in stack:
        score += x[1] * ll
        ll -= 1

    assert score == 249817836
    print(score)
