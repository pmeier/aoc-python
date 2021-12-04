import pathlib

import pytest
import yaml
from aoc.utils import load_solver


def load_test_configs(*, path=pathlib.Path(__file__).parent / "tests.yaml"):
    with open(path) as file:
        year_configs = yaml.load(file, yaml.Loader)

    params = []
    for year_id, day_configs in year_configs.items():
        year = int(year_id.replace("year", ""))
        for day_id, config in day_configs.items():
            day = int(day_id.replace("day", ""))
            input = config.pop("input").strip().splitlines()
            for part_id, expected in config.items():
                part = int(part_id.replace("part", ""))
                params.append(
                    pytest.param(
                        year,
                        day,
                        part,
                        input,
                        expected,
                        id=f"{year_id}-{day_id}-{part_id}",
                    )
                )

    return pytest.mark.parametrize(("year", "day", "part", "input", "expected"), params)


@load_test_configs()
def test_aoc(year, day, part, input, expected):
    solver = load_solver(year, day, part)
    assert solver(input) == expected
