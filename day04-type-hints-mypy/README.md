# Day 4 — Type Hints & Static Analysis

## Why this matters
Python doesn't check types at runtime unless you tell it to — you can pass a
string where a function expects an int and it'll happily run until it crashes
somewhere confusing three function calls later. Type hints don't change how
Python runs; they let a separate tool (`mypy`) read your code *without running
it* and catch that class of bug before you ever hit "run." This is different
from today's earlier days — today is 100% about a *static* tool, not pytest.

## Where you'll actually use this
- **Every FastAPI endpoint you write from Week 3 onward is type-hinted** —
  FastAPI literally uses your type hints to generate request validation and
  the `/docs` page. This isn't optional style there; it's load-bearing.
- **Any codebase with more than one contributor**: type hints are how you
  document what a function expects without writing prose that goes stale.
  Most production Python codebases (and every serious backend job you'd
  interview for) run mypy or a similar checker in CI.
- **Refactoring safety net**: when you change a function's signature, mypy
  immediately shows you every call site that's now wrong — before you'd find
  out from a crash in production.

## Concepts & syntax

### Basic hints
```python
def add(a: int, b: int) -> int:
    return a + b
```
`a: int` and `b: int` say what the parameters should be; `-> int` says what
the function returns. None of this is enforced at runtime — it's purely for
mypy (and your editor) to read.
Docs: https://docs.python.org/3/library/typing.html

### Collections
```python
def total(nums: list[int]) -> int:
    ...

def lookup(people: dict[str, int]) -> int | None:
    ...
```
`list[int]` means "a list where every element is an int." `dict[str, int]`
means "keys are str, values are int." (In Python 3.9+ you can use the
lowercase builtins directly like this — older code uses `List[int]` /
`Dict[str, int]` imported from `typing`, which you'll still see a lot.)

### `Optional` / `| None`
```python
def find_user(user_id: int) -> str | None:
    ...
```
Means "returns a str, or None." This is one of the most valuable hints you
can write — it forces callers (and mypy) to consider the case where nothing
was found, instead of assuming a string always comes back.
Docs: https://docs.python.org/3/library/typing.html#typing.Optional

### Running mypy
```bash
mypy starter.py
```
Reads the file without executing it and reports every place your code and
your type hints disagree.

## The task
Open `starter.py`. It has three functions with type hint bugs: one is missing
hints entirely, one has a hint that's flat-out wrong for what the function
actually does, and one has a subtly incomplete hint. Fix all three so that:
1. `mypy starter.py` reports `Success: no issues found`
2. `pytest` still passes (the *behavior* is already correct — you're only
   fixing the hints, not the logic)

## Run it
```bash
cd day04-type-hints-mypy
mypy starter.py      # read every error message carefully first
pytest -v            # should already pass regardless of hints
```

## Common pitfalls
- mypy errors can look intimidating at first — read the file/line number and
  the actual message; it almost always tells you exactly what it expected vs.
  what it found.
- A hint can be *syntactically* fine but *semantically* wrong (like saying a
  function returns `int` when it actually returns `str`) — mypy will still
  catch this by comparing your hint against what the function body actually
  does, not just checking the syntax is valid.
- Don't reach for `Any` to make an error disappear — that turns off type
  checking for that value entirely, which defeats the point. If you're
  tempted to use `Any`, that's a sign to look up the actual correct type
  instead.

## Stretch goal (optional)
Add a `mypy.ini` file to this folder with `strict = True` and see how many
*new* errors appear on your now-passing file. Strict mode requires every
function to be fully annotated, including ones with no parameters — it's
what most serious production codebases actually run.

## Further reading
- `typing` module docs (the full reference): https://docs.python.org/3/library/typing.html
- mypy's own cheat sheet (genuinely useful, bookmark it):
  https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
