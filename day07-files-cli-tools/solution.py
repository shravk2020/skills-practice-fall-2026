import argparse
import json
import csv
from pathlib import Path
from collections import Counter


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Summarize records by category.")
    parser.add_argument("input_path", help="Path to a .json or .csv file")
    return parser.parse_args(argv)


def load_records(path):
    path = Path(path)
    if path.suffix == ".json":
        with open(path) as f:
            return json.load(f)
    elif path.suffix == ".csv":
        with open(path, newline="") as f:
            return list(csv.DictReader(f))
    else:
        raise ValueError(f"unsupported file type: {path.suffix}")


def summarize(records):
    return dict(Counter(r["category"] for r in records))


def main(argv=None):
    args = parse_args(argv)
    records = load_records(args.input_path)
    counts = summarize(records)
    for category in sorted(counts):
        print(f"{category}: {counts[category]}")


if __name__ == "__main__":
    main()
