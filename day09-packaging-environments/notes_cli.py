import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Count notes in a text file.")
    parser.add_argument("path", help="Path to a text file, one note per line.")
    return parser.parse_args(argv)


def count_notes(path):
    with open(path) as f:
        lines = [line for line in f if line.strip()]
    return len(lines)


def main(argv=None):
    args = parse_args(argv)
    count = count_notes(args.path)
    print(f"{count} notes found in {args.path}")


if __name__ == "__main__":
    main()
