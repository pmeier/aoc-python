import operator
from collections import Counter
from functools import reduce


def parse_lines(solver):
    def wrapper(lines):
        return solver(
            [
                [
                    [segment_str for segment_str in segments_strs.strip().split()]
                    for segments_strs in line.split("|")
                ]
                for line in lines
            ]
        )

    return wrapper


def make_decoding_map(inputs):
    segments = [set(input) for input in inputs]

    # digits 1, 4, 7, and 8 are uniquely identified by the number of segments
    encoding_map = {
        1: next(input for input in segments if len(input) == 2),
        4: next(input for input in segments if len(input) == 4),
        7: next(input for input in segments if len(input) == 3),
        8: next(input for input in segments if len(input) == 7),
    }

    c_and_f = encoding_map[1]
    a = encoding_map[7] - encoding_map[1]
    b_and_d = encoding_map[4] - encoding_map[1]
    e_and_g = encoding_map[8] - (encoding_map[7] | encoding_map[4])

    # all digits with 5 segments (2, 3, and 5) use the vertical segments a, d, and g
    a_and_d_and_g = reduce(
        operator.and_, [segment for segment in segments if len(segment) == 5]
    )
    d_and_g = a_and_d_and_g - a
    b_and_e = (b_and_d - d_and_g) | (e_and_g - d_and_g)

    encoding_map[3] = a_and_d_and_g | c_and_f
    # 6 is is the only 6 segment digit that has segments a, b, d, e, and g
    encoding_map[6] = next(
        segment
        for segment in segments
        if len(segment) == 6 and len(segment - (a | b_and_e | d_and_g)) == 1
    )
    c = encoding_map[8] - encoding_map[6]
    f = c_and_f - c

    # 3 and 5 are the only 5 segment digits that have segments a, d, f, g.
    # Since we know 3 already, we can isolate 5.
    encoding_map[5] = next(
        segments
        for segments in [
            input
            for input in segments
            if len(input) == 5 and len(input - (a_and_d_and_g | f)) == 1
        ]
        if segments != encoding_map[3]
    )

    b_and_f = encoding_map[5] - a_and_d_and_g
    b = b_and_f - f
    e = b_and_e - b
    d = b_and_d - b
    g = e_and_g - e

    encoding_map.update(
        {
            0: a | b | c | e | f | g,
            2: a | c | d | e | g,
            9: a | b | c | d | f | g,
        }
    )
    return {
        "".join(sorted(segments)): number for number, segments in encoding_map.items()
    }


def decode_outputs(outputs, decoding_map):
    return int(
        "".join([str(decoding_map["".join(sorted(output))]) for output in outputs])
    )


def decode(inputs_and_outputs):
    for inputs, outputs in inputs_and_outputs:
        decoding_map = make_decoding_map(inputs)
        yield decode_outputs(outputs, decoding_map)


@parse_lines
def part1(inputs_and_outputs):
    num_special_digits = 0
    for output in decode(inputs_and_outputs):
        counter = Counter(str(output))
        num_special_digits += sum(counter[str(digit)] for digit in (1, 4, 7, 8))
    return num_special_digits


@parse_lines
def part2(inputs_and_outputs):
    return sum(iter(decode(inputs_and_outputs)))
