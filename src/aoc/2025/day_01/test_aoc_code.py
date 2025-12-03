# noqa: INP001
"""AoC 2025 Day 1 test file.

uv run ./src/aoc/2025/day_01/aoc_code.py
uv run pytest ./src/aoc/2025/day_01/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_01/
"""

from .aoc_code import part1, part2  # type: ignore[import-not-found]  # mypy

# Example data for development: Part1=3, Part2=6
example_data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def test_part1() -> None:
    assert part1(example_data) == 3  # noqa: PLR2004 # acceptable for tests


def test_part2() -> None:
    assert part2(example_data) == 6  # noqa: PLR2004 # acceptable for tests
