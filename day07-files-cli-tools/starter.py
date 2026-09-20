import argparse
import json
import csv
from pathlib import Path
from collections import Counter


def parse_args(argv=None):
    """Build an argparse.ArgumentParser with one required positional
    argument, `input_path`. Return parser.parse_args(argv).

    TODO: implement.
    """
    pass


def load_records(path):
    """path is a str or Path to a .json or .csv file.
    - .json: a JSON list of objects -- return it as-is.
    - .csv: has a header row -- return a list of dicts (one per row).
    Use Path(path).suffix to decide which branch to use.

    TODO: implement.
    """
    pass


def summarize(records):
    """records is a list of dicts, each with a "category" key.
    Return a dict mapping category -> count of records with that category.

    TODO: implement using collections.Counter.
    """
    pass


def main(argv=None):
    """Wire it together:
    1. args = parse_args(argv)
    2. records = load_records(args.input_path)
    3. counts = summarize(records)
    4. print one line per category, sorted alphabetically, formatted as
       f"{category}: {count}"

    TODO: implement.
    """
    pass


if __name__ == "__main__":
    main()
