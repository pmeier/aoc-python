import argparse
import sys

from .utils import load_solver, load_input


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    input = load_input(args.year, args.day)
    solver = load_solver(args.year, args.day, args.part)
    print(solver(input))


def parse_args(args):
    parser = argparse.ArgumentParser(
        prog="aoc", description="Advent of Code solutions in Python"
    )
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)

    return parser.parse_args(args)
