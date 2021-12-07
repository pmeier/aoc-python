from math import sqrt
from statistics import median, mean


def parse_lines(fn):
    def wrapper(lines):
        return fn([int(position) for position in lines[0].split(",")])

    return wrapper


def _solve(positions, *, compute_initial_guess, compute_fuel_costs):
    initial_guess = compute_initial_guess(positions)
    fuel_costs = compute_fuel_costs(positions, initial_guess)

    for guess in range(initial_guess - 1, -1, -1):
        new_fuel_costs = compute_fuel_costs(positions, guess)
        if new_fuel_costs < fuel_costs:
            fuel_costs = new_fuel_costs
        else:
            break

    for guess in range(initial_guess + 1, max(positions) + 1):
        new_fuel_costs = compute_fuel_costs(positions, guess)
        if new_fuel_costs < fuel_costs:
            fuel_costs = new_fuel_costs
        else:
            break

    return fuel_costs


@parse_lines
def part1(positions):
    def compute_initial_guess(positions):
        return round(median(positions))

    def compute_fuel_costs(positions, guess):
        return sum(abs(guess - position) for position in positions)

    return _solve(
        positions,
        compute_initial_guess=compute_initial_guess,
        compute_fuel_costs=compute_fuel_costs,
    )


@parse_lines
def part2(positions):
    def compute_initial_guess(positions):
        return round(sqrt(mean([position ** 2 for position in positions])))

    def compute_fuel_costs(positions, guess):
        return sum(
            [
                (diff := abs(guess - position)) * (diff + 1) // 2
                for position in positions
            ]
        )

    return _solve(
        positions,
        compute_initial_guess=compute_initial_guess,
        compute_fuel_costs=compute_fuel_costs,
    )
