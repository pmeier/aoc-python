import itertools


def parse_lines(solver):
    def wrapper(lines):
        lines = iter(lines)
        dots = []
        for line in lines:
            if not line:
                break

            dots.append(tuple(int(coordinate) for coordinate in line.split(",")))

        num_cols, num_rows = [max(coordinates) + 1 for coordinates in zip(*dots)]
        paper = [[False] * num_cols for _ in range(num_rows)]
        for x, y in dots:
            paper[y][x] = True

        folds = []
        for instruction in lines:
            coordinate, idx = instruction.replace("fold along ", "").split("=")
            folds.append((coordinate, int(idx)))

        return solver(paper, folds)

    return wrapper


def fold(paper, instruction):
    coordinate, idx = instruction
    if coordinate == "x":
        paper = transpose(paper)

    bot_rows, top_rows = paper[:idx], paper[idx + 1 :]
    top_rows_reversed = list(reversed(top_rows))
    num_bot_rows = len(bot_rows)
    num_top_rows = len(top_rows_reversed)

    num_diff = num_bot_rows - num_top_rows
    if num_diff > 0:
        folded_paper, bot_rows = bot_rows[:num_diff], bot_rows[num_diff:]
    elif num_diff < 0:
        num_diff *= -1
        folded_paper, top_rows_reversed = (
            top_rows_reversed[:num_diff],
            top_rows_reversed[num_diff:],
        )
    else:
        folded_paper = []

    folded_paper.extend(
        [
            [
                bot_is_dot | top_is_dot
                for bot_is_dot, top_is_dot in zip(bot_row, top_row)
            ]
            for bot_row, top_row in zip(bot_rows, top_rows_reversed)
        ]
    )

    if coordinate == "x":
        folded_paper = transpose(folded_paper)
    return folded_paper


def transpose(paper):
    return list(zip(*paper))


def to_str(paper):
    return "\n".join(
        ["".join(["#" if is_dot else "." for is_dot in row]) for row in paper]
    )


@parse_lines
def part1(paper, instructions):
    return sum(itertools.chain(*fold(paper, instructions[0])))


@parse_lines
def part2(paper, instructions):
    for instruction in instructions:
        paper = fold(paper, instruction)

    return to_str(paper)
