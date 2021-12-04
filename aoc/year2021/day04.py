import itertools
from dataclasses import dataclass


@dataclass
class BoardNumber:
    value: int
    marked: bool = False


class Board:
    def __init__(self, board):
        self._number_map = {
            number.value: number for number in itertools.chain.from_iterable(board)
        }
        self._rows = board
        self._cols = list(zip(*board))

    def score(self, drawn_number):
        try:
            number = self._number_map[drawn_number]
        except KeyError:
            return None

        number.marked = True

        for row_or_col in itertools.chain(self._rows, self._cols):
            if all(number_.marked for number_ in row_or_col):
                return number.value * sum(
                    number.value
                    for number in self._number_map.values()
                    if not number.marked
                )


def parse_lines(fn):
    def wrapper(lines):
        draw = [int(number) for number in lines[0].split(",")]

        boards = []
        rows = []
        for line in itertools.chain(lines[2:], ("",)):
            if not line:
                boards.append(Board(rows))
                rows = []
                continue

            rows.append([BoardNumber(int(number)) for number in line.split()])

        return fn(draw, boards)

    return wrapper


@parse_lines
def part1(draw, boards):
    for drawn_number in draw:
        for board in boards:
            score = board.score(drawn_number)
            if score is not None:
                return score


@parse_lines
def part2(draw, boards):
    boards = boards.copy()
    for drawn_number in draw:
        for board in boards.copy():
            score = board.score(drawn_number)
            if score is not None:
                if len(boards) == 1:
                    return score

                boards.remove(board)
