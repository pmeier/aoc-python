import itertools
from collections import Counter, defaultdict


def parse_lines(solver):
    def wrapper(lines):
        template = list(lines[0])

        insertion_rules = {}
        for line in lines[2:]:
            pair, insert = line.split(" -> ")
            insertion_rules[tuple(pair)] = insert

        return solver(template, insertion_rules)

    return wrapper


def solve(template, insertion_rules, *, steps):
    pair_counts = Counter(itertools.pairwise(template))

    for _ in range(steps):
        for pair, count in tuple(pair_counts.items()):
            insert = insertion_rules[pair]
            pair_counts[(pair[0], insert)] += count
            pair_counts[(insert, pair[1])] += count
            pair_counts[pair] -= count

    # Since the pairs overlap, we only the second character in each pair. The first
    # character in the template would be ignored by this however.
    single_counts = defaultdict(lambda: 0, {template[0]: 1})
    for pair, count in pair_counts.items():
        single_counts[pair[1]] += count

    _, most_common = zip(*Counter(single_counts).most_common())
    return most_common[0] - most_common[-1]


@parse_lines
def part1(template, insertion_rules):
    return solve(template, insertion_rules, steps=10)


@parse_lines
def part2(template, insertion_rules):
    return solve(template, insertion_rules, steps=40)
