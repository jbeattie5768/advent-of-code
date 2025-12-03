# noqa: INP001
"""AoC 2025 Day 12 test file.

uv run ./src/aoc/2025/day_12/aoc_code.py
uv run pytest ./src/aoc/2025/day_12/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_12/
"""

from .aoc_code import part1, part2  # type: ignore[import-not-found]  # mypy

example_data = [""]  # Add example data here for development

def test_part1() -> None:
    assert part1(example_data) == 0

def test_part2() -> None:
    assert part2(example_data) == 0

