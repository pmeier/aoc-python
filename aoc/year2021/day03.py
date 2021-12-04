import functools
from collections import Counter


def part1(lines):
    gamma_rate = 0
    for idx, bits in enumerate(reversed(tuple(zip(*lines)))):
        gamma_rate |= int(Counter(bits).most_common(1)[0][0]) << idx

    delta_rate = gamma_rate ^ (2 ** len(lines[0]) - 1)

    return gamma_rate * delta_rate


def compute_generator_rating(lines, *, bit_selector):
    lines = lines.copy()
    idx = 0
    while len(lines) > 1:
        bit = bit_selector(Counter(tuple(zip(*lines))[idx]))
        lines = [line for line in lines if line[idx] == bit]
        idx += 1

    return int(lines[0], 2)


def select_oxygen_generator_bit(counter):
    return "1" if counter["0"] == counter["1"] else counter.most_common(1)[0][0]


compute_oxygen_generator_rating = functools.partial(
    compute_generator_rating, bit_selector=select_oxygen_generator_bit
)


def select_c02_generator_bit(counter):
    return (
        "0"
        if counter["0"] == counter["1"]
        else ({"0", "1"} - {counter.most_common(1)[0][0]}).pop()
    )


compute_co2_generator_rating = functools.partial(
    compute_generator_rating, bit_selector=select_c02_generator_bit
)


def part2(lines):
    return compute_oxygen_generator_rating(lines) * compute_co2_generator_rating(lines)
