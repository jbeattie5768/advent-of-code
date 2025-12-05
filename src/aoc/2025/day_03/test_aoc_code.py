# noqa: INP001
"""AoC 2025 Day 3 test file.

uv run ./src/aoc/2025/day_03/aoc_code.py
uv run pytest ./src/aoc/2025/day_03/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_03/
"""

from .aoc_code import part1, part2  # type: ignore[import-not-found]  # mypy

example_data_part1 = [
    "987654321111111",  # largest joltage possible, 98 (9 and 8)
    "811111111111119",  # Largest joltage possible, 89 (8 and 9)
    "234234234234278",  # Largest joltage possible, 78 (7 and 8)
    "818181911112111",  # largest joltage you can produce is 92 (9 and 2)
]  #  sum of the max joltage from each bank is 98 + 89 + 78 + 92 = 357

example_data_part2 = [
    "987654321111111",  # largest 12 digit joltage possible, 987654321111
    "811111111111119",  # Largest 12 digit joltage possible, 811111111119
    "234234234234278",  # Largest 12 digit joltage possible, 434234234278
    "818181911112111",  # largest 12 digit joltage you can produce is 888911112111
]  #  sum of the max joltage from each bank is 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619


def test_part1() -> None:
    assert part1(example_data_part1) == 357  # noqa: PLR2004


def test_part2() -> None:
    assert part2(example_data_part2) == 3121910778619  # noqa: PLR2004
