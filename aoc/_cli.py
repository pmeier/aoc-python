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
    # FIXME: implement actual argument parsing
    return argparse.Namespace(year=2021, day=4, part=2)
