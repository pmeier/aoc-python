from itertools import tee, islice


def parse_lines(fn):
    def wrapper(lines):
        return fn([int(depth) for depth in lines])

    return wrapper


def group(iterable, *, n):
    return zip(
        *[
            islice(iterator, start, None)
            for start, iterator in enumerate(tee(iterable, n))
        ]
    )


@parse_lines
def part1(depths):
    return sum([depth2 > depth1 for depth1, depth2 in group(depths, n=2)])


@parse_lines
def part2(depths):
    return sum(
        [
            sum(depths2) > sum(depths1)
            for depths1, depths2 in group(group(depths, n=3), n=2)
        ]
    )
