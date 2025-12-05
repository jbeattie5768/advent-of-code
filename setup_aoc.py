"""Script to setup Advent of Code (AoC) folders and fetch input data.

uv run python ./setup_aoc.py

usage: setup_aoc.py [-h] [-i Days Year] [-f Day Year]

options:
  -h, --help            show this help message and exit
  -i, --init Days Year  create 'days' folders under 'year' folder, e.g. -i 12 2025
  -f, --fetch Day Year  get AoC input data for given 'day' and 'year', e.g. -f 1 2025

Examples:
uv run python ./setup_aoc.py -i 12 2025  # create folders for days 1-12 for year 2025
uv run python ./setup_aoc.py -f 1 2025   # fetch input data for day 1 of year 2025

"""

import argparse
import datetime
import os
import sys
from pathlib import Path

from aocd import get_data

AOC_MAX_DAYS = 25  # 2015-2024
# AOC_MAX_DAYS = 12  # 2025-
AOC_START_YEAR = 2015
CENTURY = 100  # used for checking if year is 2-digits

token = ""
# Get the AOC Session Token from file
with Path(".session.txt").open("r") as fid:
    token = fid.read().strip()
# ...alternatively you can get it from an ENV
# token = os.getenv("AOC_SESSION_TOKEN", token)


def args_parser(arg_list: list[str] | None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--init",
        nargs=2,
        metavar=("Days", "Year"),
        help="create 'days' folders under 'year' folder, e.g. -i 12 2025",
    )

    parser.add_argument(
        "-f",
        "--fetch",
        nargs=2,
        metavar=("Day", "Year"),
        help="get AoC input data for given 'day' and 'year', e.g. -f 1 2025",
    )

    if arg_list is None or len(arg_list) == 1:  # no args
        parser.print_help()  # default to stdout, can be redirected 'sys.stderr'
        sys.exit(1)

    args: argparse.Namespace = parser.parse_args(arg_list)

    return args


def check_days_year(days: int, year: int) -> tuple[int, int]:
    """Simple checks for valid day(s) and year."""
    current_date = datetime.datetime.now(tz=datetime.UTC).date()
    current_year = current_date.year

    if days == 0 or days > AOC_MAX_DAYS:  # if not 1-25
        print(f"Restricted {days} days to AOC max {AOC_MAX_DAYS} days")
        days = AOC_MAX_DAYS

    if year < CENTURY:  # 2 digit year
        print(f"Assuming year {year} was {year + 2000}")
        year += 2000

    if year < AOC_START_YEAR or year > current_year:  # if not 2015-2025+
        print(f"Year {year} outside AOC years, changed to year {current_year}")
        year = current_year

    return (days, year)


def create_aoc_folders(days: int, year: int) -> None:
    """Create AoC folder structure for given year and number of days.

    A boilerplate 'aoc_code.py' and 'test_aoc_code.py' file is created in each day folder.
    Will not overwrite existing folders/files.
    """
    days, year = check_days_year(days, year)

    folder_year = f"{year}"
    root_path = "./src/aoc"
    os.chdir(root_path)

    # Initialize '__init__.py' in src/aoc if not present
    if not Path("__init__.py").exists():
        with Path("__init__.py").open("w") as fid:
            fid.write("")

    # Create year folder if not present
    if not Path(folder_year).exists():
        Path(folder_year).mkdir()

    os.chdir(folder_year)

    # Create day folders if not present
    for day in range(1, days + 1):
        folder_day = f"day_{day:02}"

        if not Path(folder_day).exists():
            Path(folder_day).mkdir()

        os.chdir(folder_day)

        # Create code file from template if not present
        if not Path("aoc_code.py").exists():
            with Path("aoc_code.py").open("w") as fid:
                fid.write(f"""# noqa: INP001
\"\"\"AoC {year} Day {day} test file.

uv run ./src/aoc/{year}/day_{day:02}/aoc_code.py
uv run pytest ./src/aoc/{year}/day_{day:02}/ -rs -v
uv run mypy --strict ./src/aoc/{year}/day_{day:02}/
\"\"\"

from pathlib import Path

example_data = [""]  # Add example data here for development

def read_data() -> list[str]:
    file_dir = Path(__file__).parent
    return Path(f"{{file_dir}}/input.txt").open("r").read().splitlines()

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

""")
        # Create test file from template if not present
        if not Path("test_aoc_code.py").exists():
            with Path("test_aoc_code.py").open("w") as fid:
                fid.write(f"""# noqa: INP001
\"\"\"AoC {year} Day {day} test file.

uv run ./src/aoc/{year}/day_{day:02}/aoc_code.py
uv run pytest ./src/aoc/{year}/day_{day:02}/ -rs -v
uv run mypy --strict ./src/aoc/{year}/day_{day:02}/
\"\"\"

from .aoc_code import part1, part2  # type: ignore[import-not-found]  # mypy

example_data = [""]  # Add example data here for development

def test_part1() -> None:
    assert part1(example_data) == 0

def test_part2() -> None:
    assert part2(example_data) == 0

""")

        os.chdir("..")  # year folder

    print(f"Completed creating {year} folder and {days} day folders")
    os.chdir("..")  # src folder
    os.chdir("..")  # root folder


def fetch_aoc_data(token: str, fetch_day: int, fetch_year: int) -> None:
    """Fetch AoC input data for given day and year, write to 'input.txt' file.

    File is written to the appropriate folder './src/aoc/YYYY/day_DD/input.txt'.
    Will overwrite existing file without warning.
    Uses the 'aocd' package to fetch the data.
    """
    fetch_day, fetch_year = check_days_year(fetch_day, fetch_year)

    with Path(f"./src/aoc/{fetch_year}/day_{fetch_day:02}/input.txt").open("w", newline="\n") as fid:
        aoc_data = get_data(session=token, day=fetch_day, year=fetch_year)
        fid.write(aoc_data + "\n")

    print(f"AoC input data file written to ./src/aoc/{fetch_year}/day_{fetch_day:02}/input.txt")


def main(arg_list: list[str] | None = None) -> None:
    """CLI entrypoint."""
    args = args_parser(arg_list)
    if args.init:
        days, year = args.init
        create_aoc_folders(int(days), int(year))

    if args.fetch:
        day, year = args.fetch
        fetch_aoc_data(token, int(day), int(year))


if __name__ == "__main__":
    print("Starting AoC setup...")
    main(sys.argv[1:])

    # main(["-i", "1", "2024"])
    # main(["-f", "5", "2025"])
