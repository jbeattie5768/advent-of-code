# noqa: INP001
"""AoC 2025 Day 2 test file.

uv run ./src/aoc/2025/day_02/aoc_code.py
uv run pytest ./src/aoc/2025/day_02/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_02/
"""

import re
from pathlib import Path

# Needed some help from CoPilot to get the regex patterns right!
# Need to refresh my regex skills.
PATTERN_PART1 = re.compile(r"^(.+?)\1$")
# ^ and $ anchor the match to the start and end of the string
# (.+?) captures the shortest sequence of one or more characters (non-greedy/lazy)
# \1 matches the same characters as the first group, immediately following

PATTERN_PART2 = re.compile(r"^(.+?)\1+$")
# ^ and $ anchor the match to the start and end of the string
# (.+?) captures the shortest sequence of one or more characters (non-greedy/lazy)
# \1+ matches one or more repetitions of the sequence captured in group 1

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


def read_data() -> list[str]:
    file_dir = Path(__file__).parent
    return Path(f"{file_dir}/input.txt").open("r").read().split(",")


def part1(data: list[str]) -> int:
    """The tricky part  was getting the regex right.

    We are looking for invalid IDs by looking for any ID
    which is made only of some sequence of digits **repeated twice**.
    This means that the length of the ID string must be even.

    """
    invalid_ids: list[int] = []

    for d_entry in data:
        start_str, end_str = d_entry.split("-")

        for test_id in range(int(start_str), int(end_str) + 1):
            test_id_str = str(test_id)
            match = bool(PATTERN_PART1.match(test_id_str))

            # if match and len(test_id_str) % 2 == 0:
            if match:  # Updated RegEx for even length
                invalid_ids.append(test_id)
                # print(f"invalid ID found: {test_id}")

    sum_invalid_ids = sum(invalid_ids)
    print(f"sum of invalid_ids: {sum_invalid_ids}")

    return sum_invalid_ids


def part2(data: list[str]) -> int:
    """Now we are looking for invalid IDs made of some sequence of digits.

    The sequence can be of any length as long as it is repeated.

    """
    invalid_ids: list[int] = []

    for d_entry in data:
        start_str, end_str = d_entry.split("-")

        for test_id in range(int(start_str), int(end_str) + 1):
            test_id_str = str(test_id)
            match = bool(PATTERN_PART2.match(test_id_str))

            if match:  # RegEx handles any length
                invalid_ids.append(test_id)
                # print(f"invalid ID found: {test_id}")

    sum_invalid_ids = sum(invalid_ids)
    print(f"sum of invalid_ids: {sum_invalid_ids}")

    return sum_invalid_ids


if __name__ == "__main__":
    res_part1 = part1(example_data_part1)  # 1227775554
    res_part2 = part2(example_data_part2)  # 4174379265
    res_part1 = part1(read_data())  # My result was 44854383294
    res_part2 = part2(read_data())  # My result was 55647141923

    # Not tried these....yet
    # data = get_data(1, 2025)  # aocd to get data
    # aocd.submit(res_part1, part="a", day=1, year=2025)
    # aocd.submit(res_part2, part="b", day=1, year=2025)
