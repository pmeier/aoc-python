from collections import defaultdict


def parse_lines(fn):
    def wrapper(lines):
        steps = []
        for line in lines:
            direction, value = line.split()
            steps.append((direction, int(value)))
        return fn(steps)

    return wrapper


@parse_lines
def part1(steps):
    bar = defaultdict(lambda: 0)
    for direction, value in steps:
        bar[direction] += value

    position = bar["forward"]
    depth = bar["down"] - bar["up"]
    return position * depth


@parse_lines
def part2(steps):
    position = depth = aim = 0
    for direction, value in steps:
        if direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        else:
            position += value
            depth += aim * value

    return position * depth
