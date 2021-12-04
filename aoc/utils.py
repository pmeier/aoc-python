import importlib
import pathlib


def load_solver(year: int, day: int, part: int):
    return getattr(
        importlib.import_module(f"aoc.year{year}.day{day:02d}"), f"part{part}"
    )


def load_input(year: int, day: int):
    with open(
        pathlib.Path(__file__).parent / f"year{year}" / "input" / f"day{day:02d}"
    ) as file:
        return file.read().strip().splitlines()
