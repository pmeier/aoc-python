import itertools
from dataclasses import dataclass


@dataclass
class LineSegment:
    start: tuple[int, int]
    stop: tuple[int, int]

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

        if start[0] == stop[0]:
            orientation = "horizontal"
            x = start[0]
            ys = (start[1], stop[1])
            coverage = [(x, y) for y in range(min(ys), max(ys) + 1)]
        elif start[1] == stop[1]:
            orientation = "vertical"
            xs = (start[0], stop[0])
            y = start[1]
            coverage = [(x, y) for x in range(min(xs), max(xs) + 1)]
        else:
            orientation = "diagonal"
            coverage = list(
                zip(
                    *[
                        range(
                            start[idx],
                            stop[idx] + (step := 1 if start[idx] < stop[idx] else -1),
                            step,
                        )
                        for idx in (0, 1)
                    ]
                )
            )

        self.orientation = orientation
        self.coverage = coverage

    @classmethod
    def from_str(cls, string):
        return cls(
            *[
                tuple(int(coordinate) for coordinate in point.strip().split(","))
                for point in string.split("->")
            ]
        )


def parse_lines(fn):
    def wrapper(lines):
        line_segments = [LineSegment.from_str(line) for line in lines]

        x_max, y_max = [
            max(
                itertools.chain.from_iterable(
                    [
                        (line_segment.start[idx], line_segment.stop[idx])
                        for line_segment in line_segments
                    ]
                )
            )
            + 1
            for idx in (0, 1)
        ]
        grid = [[0] * x_max for _ in range(y_max)]

        return fn(grid, line_segments)

    return wrapper


@parse_lines
def part1(grid, line_segments):
    for line_segment in line_segments:
        if line_segment.orientation not in ("horizontal", "vertical"):
            continue

        for point in line_segment.coverage:
            x, y = point
            grid[y][x] += 1

    return sum(coverage >= 2 for coverage in itertools.chain.from_iterable(grid))


@parse_lines
def part2(grid, line_segments):
    for line_segment in line_segments:
        for point in line_segment.coverage:
            x, y = point
            grid[y][x] += 1

    return sum(coverage >= 2 for coverage in itertools.chain.from_iterable(grid))
