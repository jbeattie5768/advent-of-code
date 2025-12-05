# noqa: INP001
"""AoC 2025 Day 3 test file.

uv run ./src/aoc/2025/day_03/aoc_code.py
uv run pytest ./src/aoc/2025/day_03/ -rs -v
uv run mypy --strict ./src/aoc/2025/day_03/
"""

from pathlib import Path

example_data_part1 = [
    "987654321111111",  # largest 2 digit joltage possible, 98 (9 and 8)
    "811111111111119",  # Largest 2 digit joltage possible, 89 (8 and 9)
    "234234234234278",  # Largest 2 digit joltage possible, 78 (7 and 8)
    "818181911112111",  # largest 2 digit joltage you can produce is 92 (9 and 2)
]  #  sum of the max joltage from each bank is 98 + 89 + 78 + 92 = 357

example_data_part2 = [
    "987654321111111",  # largest 12 digit joltage possible, 987654321111
    "811111111111119",  # Largest 12 digit joltage possible, 811111111119
    "234234234234278",  # Largest 12 digit joltage possible, 434234234278
    "818181911112111",  # largest 12 digit joltage you can produce is 888911112111
]  #  sum of the max joltage from each bank is 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619


def read_data() -> list[str]:
    file_dir = Path(__file__).parent
    return Path(f"{file_dir}/input.txt").open("r").read().splitlines()


def part1(data: list[str]) -> int:
    """Find the highest joltage you can produce from each bank.

    Each bank can produce a joltage by combining any two of its batteries.
    The joltage produced is the two batteries' value *concatenated* together.
    The batteries can only be sequentially connected, so the order matters.
    The highest joltage from each bank is then summed to produce the final result.

    """
    max_joltage = 0
    for bank in data:
        # Find the largest adapter in the bank
        largest_battery = max(bank[:-1])  # except last value
        battery_index = bank.index(largest_battery)
        # From that point onward, find the next largest adapter
        # Could create a new string, but we have no idea how big the banks are
        next_battery = 0
        for i in range(battery_index + 1, len(bank)):
            next_battery = max(next_battery, int(bank[i]))

        joltage = int(f"{largest_battery}{next_battery}")
        # print(f"Bank: {bank}, Largest: {largest_battery}, Next: {next_battery}, Joltage: {joltage}")
        max_joltage += joltage

    print(f"Part 1: Max Joltage = {max_joltage}")

    return max_joltage


def part2(data: list[str]) -> int:
    """Find the highest 12-digit joltage you can produce from each bank.

    The order still matters, but you can use any combination of batteries
    to produce a 12-digit joltage.
    The highest joltage from each bank is then summed to produce the final result.

    """
    sum_joltage = 0
    for bank in data:
        # Greedy approach: for each position, pick the largest possible digit
        battery_digits: list[str] = []
        start_index = 0
        batteries_remaining = 12
        while batteries_remaining > 0:
            # Find largest digit in the range that allows enough digits left
            end_index = len(bank) - batteries_remaining + 1
            max_digit = max(bank[start_index:end_index])
            # Find the first occurrence of max_digit in allowed range
            idx = bank.index(max_digit, start_index, end_index)
            battery_digits.append(max_digit)
            start_index = idx + 1
            batteries_remaining -= 1
            # print(f"Bank: {bank}, Digit: {max_digit}, Remaining: {batteries_remaining}")

        sum_joltage += int("".join(battery_digits))

    print(f"Part 2: Max Joltage = {sum_joltage}")

    return int(sum_joltage)


if __name__ == "__main__":
    # res_part1 = part1(example_data_part1)
    # res_part2 = part2(example_data_part2)
    res_part1 = part1(read_data())  # My result 17031
    res_part2 = part2(read_data())  # My result 168575096286051

    # Not tried these....yet
    # data = get_data(1, 2025)  # aocd to get data
    # aocd.submit(res_part1, part="a", day=1, year=2025)
    # aocd.submit(res_part2, part="b", day=1, year=2025)
