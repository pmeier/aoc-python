from collections import Counter, deque


def parse_lines(fn):
    def wrapper(lines):
        return fn([int(initial_state) for initial_state in lines[0].split(",")])

    return wrapper


def solve(initial_states, *, days):
    counter = Counter(initial_states)
    fishs = deque([counter.get(state, 0) for state in range(9)])
    for _ in range(days):
        fishs.rotate(-1)
        fishs[6] += fishs[8]
    return sum(fishs)


@parse_lines
def part1(initial_states):
    return solve(initial_states, days=80)


@parse_lines
def part2(initial_states):
    return solve(initial_states, days=256)
