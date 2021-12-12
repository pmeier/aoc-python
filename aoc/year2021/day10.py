from queue import LifoQueue
from statistics import median

OPENING_CHARS, CLOSING_CHARS = zip(
    *(
        ("(", ")"),
        ("[", "]"),
        ("{", "}"),
        ("<", ">"),
    )
)

OPENING_CHAR_MAP = dict(zip(OPENING_CHARS, CLOSING_CHARS))
CLOSING_CHAR_MAP = dict(zip(CLOSING_CHARS, OPENING_CHARS))

ILLEGAL_CHAR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def part1(lines):
    illegal_chars = []
    for line in lines:
        q = LifoQueue()
        for char in line:
            if char in ("(", "[", "{", "<"):
                q.put(char)
            elif CLOSING_CHAR_MAP[char] != q.get():
                illegal_chars.append(char)
                break

    return sum([ILLEGAL_CHAR_SCORES[char] for char in illegal_chars])


COMPLETE_CHAR_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def part2(lines):
    completions = []
    for line in lines:
        q = LifoQueue()
        for char in line:
            if char in ("(", "[", "{", "<"):
                q.put(char)
            elif CLOSING_CHAR_MAP[char] != q.get():
                break
        else:
            completions.append(
                "".join([OPENING_CHAR_MAP[char] for char in reversed(q.queue)])
            )

    completion_scores = []
    for completion in completions:
        score = 0
        for char in completion:
            score = score * 5 + COMPLETE_CHAR_SCORE[char]
        completion_scores.append(score)

    return median(completion_scores)
