# Day 7 — Files & CLI Tools

## Why this matters
Real scripts take input from somewhere other than a hardcoded string in the
source code — a file path passed on the command line, a JSON or CSV file
someone hands you, a config file. Today combines `argparse` (reading command-
line arguments), `pathlib` (working with file paths without string-hacking),
and `json`/`csv` (reading real data formats) into one small but complete tool.

## Where you'll actually use this
- **Every project this entire 8-week plan builds from here on** touches
  files, paths, or CLI args in some way — this is infrastructure, not a
  one-off skill.
- **Data science / ML work**: loading a dataset from a CSV/JSON file you
  didn't write is the single most common first step in any analysis or
  training script.
- **DevOps/scripting roles**: CLI tools that take a file path and produce a
  report are an extremely common "take-home" or internship task.

## Concepts & syntax

### `argparse`
```python
import argparse

parser = argparse.ArgumentParser(description="Summarize a file.")
parser.add_argument("input_path", help="Path to a .json or .csv file")
args = parser.parse_args()
print(args.input_path)
```
`add_argument("input_path", ...)` (no leading dashes) creates a *required
positional* argument — the user just types `python3 tool.py somefile.json`,
no flag needed. Compare to `add_argument("--verbose", action="store_true")`,
which creates an *optional flag*. Passing `argv` explicitly to
`parser.parse_args(argv)` (instead of leaving it as `None`, which reads
`sys.argv`) is what makes this testable — you can call your parsing function
directly from a test with a fake argument list.
Docs: https://docs.python.org/3/library/argparse.html

### `pathlib.Path`
```python
from pathlib import Path

p = Path("data/records.json")
p.suffix        # ".json"
p.exists()      # True/False
p.read_text()   # reads the whole file as a string
```
Modern Python code uses `Path` instead of manually joining strings with `/`
or checking extensions with `.endswith(...)`. `.suffix` is the idiomatic way
to check a file's extension.
Docs: https://docs.python.org/3/library/pathlib.html

### Reading JSON
```python
import json
with open(path) as f:
    data = json.load(f)     # returns whatever the JSON was: list, dict, etc.
```
Docs: https://docs.python.org/3/library/json.html

### Reading CSV as dicts
```python
import csv
with open(path, newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)    # each row is a dict using the header row as keys
```
`DictReader` uses the first row as column names automatically — you get a
list of dicts instead of a list of plain lists, which is almost always what
you actually want.
Docs: https://docs.python.org/3/library/csv.html#csv.DictReader

## The task
Open `starter.py`. Implement:
1. `parse_args(argv=None)` — one required positional argument, `input_path`.
2. `load_records(path)` — reads a `.json` file (a JSON list of objects) or a
   `.csv` file (with a header row) and returns a list of dicts either way,
   based on `Path(path).suffix`.
3. `summarize(records)` — takes that list of dicts (each has a `"category"`
   key) and returns a dict of `category -> count`.
4. `main(argv=None)` — wires it together: parse args, load, summarize, then
   print one line per category **sorted alphabetically**, formatted exactly
   as `f"{category}: {count}"`.

## Run it
```bash
cd day07-files-cli-tools
pytest -v
```
The tests use pytest's built-in `tmp_path` fixture to create real temporary
files on disk, so you're testing actual file I/O, not just in-memory data.

Once tests pass, also try it for real from the command line:
```bash
echo '[{"category": "bug"}, {"category": "feature"}, {"category": "bug"}]' > /tmp/sample.json
python3 starter.py /tmp/sample.json
```

## Common pitfalls
- CSV values are **always strings**, even if they look like numbers
  (`"1"`, not `1`) — `csv.DictReader` doesn't guess types for you. This is
  realistic: real-world CSV parsing bugs are very often "why is this a
  string" bugs.
- Forgetting `newline=""` when opening a CSV file on some platforms can cause
  extra blank rows — it's a one-line habit worth having every time you touch
  `csv`.
- `argparse` positional arguments are required by default — if you want an
  optional one, you need `nargs="?"` or a `--flag` instead.

## Stretch goal (optional)
Add an optional `--top N` flag (`action` isn't right here — use
`type=int, default=None`) that, when provided, only prints the N most common
categories instead of all of them (use `collections.Counter.most_common(N)`).

## Further reading
- `argparse` tutorial (friendlier than the full reference):
  https://docs.python.org/3/howto/argparse.html
- `pathlib` cheat sheet: https://docs.python.org/3/library/pathlib.html#basic-use
