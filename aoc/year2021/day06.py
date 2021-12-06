from collections import Counter


def solve(internal_states, *, days):
    fishs = Counter(internal_states)
    for _ in range(days):
        fishs = dict(
            zip([internal_state - 1 for internal_state in fishs.keys()], fishs.values())
        )
        num_new_fish = fishs.pop(-1, 0)
        try:
            fishs[6] += num_new_fish
        except KeyError:
            fishs[6] = num_new_fish
        fishs[8] = num_new_fish

    return sum(fishs.values())


def parse_lines(fn):
    def wrapper(lines):
        return fn([int(internal_state) for internal_state in lines[0].split(",")])

    return wrapper


@parse_lines
def part1(internal_states):
    return solve(internal_states, days=80)


@parse_lines
def part2(internal_states):
    return solve(internal_states, days=256)
