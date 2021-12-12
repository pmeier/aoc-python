import itertools
from dataclasses import dataclass


@dataclass
class Octopus:
    idx: tuple[int, int]
    energy: int

    def energize(self):
        self.energy += 1
        return self.energy == 10

    def __hash__(self):
        return hash(self.idx)


def parse_lines(solver):
    def wrapper(lines):
        return solver(
            [
                [Octopus(idx=(i, j), energy=int(val)) for j, val in enumerate(line)]
                for i, line in enumerate(lines)
            ]
        )

    return wrapper


def get_neighbours(octopi, idx):
    return [
        octopi[i][j]
        for i, j in (
            (idx[0] + 1, idx[1] - 1),  # top left
            (idx[0] + 1, idx[1]),  # top
            (idx[0] + 1, idx[1] + 1),  # top right
            (idx[0], idx[1] + 1),  # right
            (idx[0] - 1, idx[1] + 1),  # bot right
            (idx[0] - 1, idx[1]),  # bot
            (idx[0] - 1, idx[1] - 1),  # bot left
            (idx[0], idx[1] - 1),  # left
        )
        if i in range(len(octopi)) and j in range(len(octopi[0]))
    ]


@parse_lines
def part1(octopi):
    num_flashes = 0
    for _ in range(100):
        flashing = [
            octopus for octopus in itertools.chain(*octopi) if octopus.energize()
        ]
        for octopus in flashing:
            flashing.extend(
                neighbour
                for neighbour in get_neighbours(octopi, octopus.idx)
                if neighbour.energize()
            )

        num_flashes += len(flashing)
        for octopus in flashing:
            octopus.energy = 0

    return num_flashes


@parse_lines
def part2(octopi):
    step = 0
    while True:
        flashing = [
            octopus for octopus in itertools.chain(*octopi) if octopus.energize()
        ]
        for octopus in flashing:
            flashing.extend(
                neighbour
                for neighbour in get_neighbours(octopi, octopus.idx)
                if neighbour.energize()
            )

        step += 1

        if len(flashing) == 100:
            break

        for octopus in flashing:
            octopus.energy = 0

    return step
