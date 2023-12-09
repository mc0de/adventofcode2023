def part_1():
    lines = [x.strip() for x in open('day5/input', 'r') if x != '\n']
    seeds = [int(x) for x in lines.pop(0).split(' ')[1:]]

    tiers = []
    r_tmp = []
    for line in lines[1:]:
        if line[0].isdigit():
            dst, src, l = [int(x) for x in line.split()]
            r_tmp.append((range(src, src + l), range(dst, dst + l)))
        else:
            tiers.append(r_tmp)
            r_tmp = []
    tiers.append(r_tmp)

    locs = []
    for seed in seeds:
        for tier in tiers:
            for src, dst in tier:
                if seed in src:
                    seed = dst[seed - src[0]]
                    break
        locs.append(seed)

    answer = min(locs)
    assert answer == 424490994
    print(answer)


def part_2():
    lines = [x.strip() for x in open('day5/input', 'r') if x != '\n']
    seeds = [int(x) for x in lines.pop(0).split(' ')[1:]]

    tiers = []
    r_tmp = []
    for line in lines[1:]:
        if line[0].isdigit():
            dst, src, l = line.split()
            dst = int(dst)
            src = int(src)
            l = int(l)
            r_tmp.append((range(src, src + l), range(dst, dst + l)))
        else:
            tiers.append(r_tmp)
            r_tmp = []
    tiers.append(r_tmp)

    seed_ranges = []

    for start, l in zip(seeds[0::2], seeds[1::2]):
        seed_ranges.append(range(start, start + l))

    lrange = range(0, 999_999_999)
    answer = None

    for loc in lrange:
        l_cpy = loc
        for tier in reversed(tiers):
            for src, dst in tier:
                if l_cpy in dst:
                    l_cpy = src[l_cpy - dst[0]]
                    break
        for ss in seed_ranges:
            if l_cpy in ss:
                answer = loc
                break
        if answer:
            break
    assert answer == 15290096
    print(answer)
