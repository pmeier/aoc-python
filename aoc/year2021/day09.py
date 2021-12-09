import functools
import operator
from dataclasses import dataclass


@dataclass
class Point:
    idx: tuple[int, int]
    val: int


def parse_lines(solver):
    def wrapper(lines):
        return solver(
            [
                [Point(idx=(i, j), val=int(val)) for j, val in enumerate(line)]
                for i, line in enumerate(lines)
            ]
        )

    return wrapper


def get_neighbours(height_map, idx):
    return [
        height_map[i][j]
        for i, j in (
            (idx[0], idx[1] - 1),
            (idx[0], idx[1] + 1),
            (idx[0] - 1, idx[1]),
            (idx[0] + 1, idx[1]),
        )
        if i in range(len(height_map)) and j in range(len(height_map[0]))
    ]


def find_low_points(height_map):
    low_points = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            low_point = height_map[i][j]
            neighbours = get_neighbours(height_map, low_point.idx)
            if all([low_point.val < neighbour.val for neighbour in neighbours]):
                low_points.append(low_point)
    return low_points


@parse_lines
def part1(height_map):
    return sum([low_point.val + 1 for low_point in find_low_points(height_map)])


@parse_lines
def part2(height_map):
    basins = []
    for low_point in find_low_points(height_map):
        basin_points = [low_point]
        for basin_point in iter(basin_points):
            basin_points.extend(
                [
                    neighbour
                    for neighbour in get_neighbours(height_map, basin_point.idx)
                    if neighbour not in basin_points
                    and neighbour.val > basin_point.val
                    and neighbour.val < 9
                ]
            )
        basins.append(basin_points)

    return functools.reduce(
        operator.mul, sorted([len(basin_points) for basin_points in basins])[-3:]
    )
