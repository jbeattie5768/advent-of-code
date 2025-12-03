# noqa: INP001
"""AoC 2025 Day 1 code file.

uv run ./src/aoc/2025/day_01/aoc_code.py
uv run pytest ./src/aoc/2025/day_01/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_01/
"""

from pathlib import Path

# Example data for development: Part1=3, Part2=6
example_data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def read_data() -> list[str]:
    """Reads 'input.txt' file from same folder as this file.

    The file is expected to be the raw data as this file returns the data as a
    list of strings.
    """
    file_dir = Path(__file__).parent
    # print(f"Reading 'input.txt' from folder: {file_dir}")
    return Path(f"{file_dir}/input.txt").open("r").read().splitlines()


def part1(data: list[str]) -> int:
    count_zeroes = 0
    curr_pos = 50

    for rotation in data:
        lor: str = rotation[0].upper()  # 'L' or 'R'
        value = int(rotation[1:])

        direction: int = -1 if lor == "L" else 1

        for _ in range(value):  # count each click
            curr_pos = curr_pos + direction
            curr_pos %= 100  # wrap to 0 if curr_pos is 100

        if curr_pos == 0:
            count_zeroes += 1

    print(f"Part 1: {count_zeroes}")
    return count_zeroes


def part2(data: list[str]) -> int:
    count_zeroes = 0
    curr_pos = 50

    for rotation in data:
        lor = rotation[0].upper()
        value = int(rotation[1:])

        lor_direct: int = -1 if lor == "L" else 1

        for _ in range(value):
            curr_pos = curr_pos + lor_direct
            curr_pos %= 100

            if curr_pos == 0:
                count_zeroes += 1

    print(f"Part 2: {count_zeroes}")

    return count_zeroes


if __name__ == "__main__":
    # res_part1 = part1(example_data)
    # res_part2 = part2(example_data)
    res_part1 = part1(read_data())  # My result was 962
    res_part2 = part2(read_data())  # My result was 5782

    # Not tried these....yet
    # data = get_data(1, 2025)  # aocd to get data
    # aocd.submit(res_part1, part="a", day=1, year=2025)
    # aocd.submit(res_part2, part="b", day=1, year=2025)
