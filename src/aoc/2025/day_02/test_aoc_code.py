# noqa: INP001
"""AoC 2025 Day 2 test file.

uv run ./src/aoc/2025/day_02/aoc_code.py
uv run pytest ./src/aoc/2025/day_02/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_02/
"""

from .aoc_code import part1, part2  # type: ignore[import-not-found]  # mypy

example_data_part1 = [
    "11-22",  # two invalid IDs: 11, 22
    "95-115",  # one invalid ID: 99
    "998-1012",  # one invalid ID: 1010
    "1188511880-1188511890",  # one invalid ID: 1188511885
    "222220-222224",  # one invalid ID: 222222
    "1698522-1698528",  # no invalid IDs
    "446443-446449",  # one invalid ID: 446446
    "38593856-38593862",  # one invalid ID: 38593859
    "565653-565659",  # no invalid IDs
    "824824821-824824827",  # no invalid IDs
    "2121212118-2121212124",  # no invalid IDs
]  # sum of all the invalid IDs in this example produces 1227775554

example_data_part2 = [
    "11-22",  # two invalid IDs, 11 and 22.
    "95-115",  # two invalid IDs, 99 and 111.
    "998-1012",  # two invalid IDs, 999 and 1010.
    "1188511880-1188511890",  # one invalid ID, 1188511885.
    "222220-222224",  # one invalid ID, 222222.
    "1698522-1698528",  # no invalid IDs.
    "446443-446449",  # one invalid ID, 446446.
    "38593856-38593862",  # sone invalid ID, 38593859.
    "565653-565659",  # one invalid ID, 565656.
    "824824821-824824827",  # one invalid ID, 824824824.
    "2121212118-2121212124",  # one invalid ID, 2121212121.
]  # sum of all the invalid IDs in this example produces 4174379265


def test_part1() -> None:
    assert part1(example_data_part1) == 1227775554  # noqa: PLR2004 # ok for tests


def test_part2() -> None:
    assert part2(example_data_part2) == 4174379265  # noqa: PLR2004 # ok for tests
