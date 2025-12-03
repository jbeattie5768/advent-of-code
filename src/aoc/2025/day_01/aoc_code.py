# noqa: INP001
"""AoC 2025 Day 1 test file.

uv run ./src/aoc/2025/day_01/aoc_code.py
uv run pytest ./src/aoc/2025/day_01/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_01/
"""

from pathlib import Path

example_data = [""]  # Add example data here for development

def read_data() -> list[str]:
    file_dir = Path(__file__).parent
    return Path(f"{file_dir}input.txt").open("r").read().splitlines()

def part1(data: list[str]) -> int:
    return 0

def part2(data: list[str]) -> int:
    return 0

if __name__ == "__main__":
    res_part1 = part1(example_data)
    #res_part2 = part2(example_data)
    # res_part1 = part1(read_data())
    # res_part2 = part2(read_data())

    # Not tried these....yet
    # data = get_data(1, 2025)  # aocd to get data
    # aocd.submit(res_part1, part="a", day=1, year=2025)
    # aocd.submit(res_part2, part="b", day=1, year=2025)

