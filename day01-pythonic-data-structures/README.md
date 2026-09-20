# Day 1 — Pythonic Data Structures

## Why this matters
Python gives you shortcuts for extremely common operations: filtering a list,
transforming every item in a list, building a lookup table, walking two lists
together. Writing these as manual `for` loops works, but it's slower to read,
slower to write, and it's one of the fastest tells — in a code review or an
interview — that someone hasn't spent much time in Python yet. Today is about
retraining your instincts so the idiomatic version is the *first* thing you
reach for, not something you translate to afterward.

## Where you'll actually use this
- **Data pipelines / ETL scripts** (very common in ML and data engineering roles):
  reshaping API responses, filtering rows, building `id -> record` lookup dicts
  from a list of database rows.
- **Technical interviews**: comprehensions are the single most common "clean code"
  signal interviewers look for in a Python screen — including the ADC-style
  interview you just did.
- **Any FastAPI/Django route** that takes a list of DB rows and reshapes them into
  JSON — you'll write this pattern constantly starting Week 3.

## Concepts & syntax

### List comprehension
```python
squares = [x * x for x in range(10)]
evens_only = [x for x in nums if x % 2 == 0]
```
Read it right-to-left-ish: "for x in nums, if x is even, keep x*x." **When to use
it:** any time you're building a new list from an existing iterable with a simple
transform and/or filter. **When *not* to:** if the body needs multiple statements,
nested `if/else` logic, or has side effects (like printing or appending to
something else) — that's a sign you want a plain loop instead. A comprehension
that needs a comment to explain it has gone too far.
Docs: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

### Dict comprehension
```python
lookup = {id_: name for id_, name in people}
```
Same idea, but builds a dict instead of a list. Extremely common for turning a
list of `(key, value)` pairs or a list of objects into an `id -> object` lookup
table so you can do O(1) lookups instead of scanning a list every time.
Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
(comprehension syntax is covered right after list comprehensions on that page)

### `enumerate()`
```python
for i, item in enumerate(items):
    print(i, item)
```
Gives you the index *and* the value together. **Never** write
`for i in range(len(items)): item = items[i]` — that's the #1 "not idiomatic yet"
pattern. If you find yourself manually incrementing a counter variable in a loop,
you almost certainly want `enumerate`.
Docs: https://docs.python.org/3/library/functions.html#enumerate

### `zip()`
```python
for name, score in zip(names, scores):
    ...
```
Walks two (or more) iterables together, pair by pair. Stops at the shorter one if
they're different lengths — that's usually fine, just know it's happening silently
rather than raising an error.
Docs: https://docs.python.org/3/library/functions.html#zip

### Tuple unpacking
```python
first, second = my_pair
id_, name = person_tuple
```
Instead of `pair[0]`, `pair[1]`. Also works in loops (`for id_, name in people:`)
and function returns (`return min_val, max_val`).
Docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

## The task
Open `starter.py`. There are three functions written the "naive" way with manual
loops and a docstring saying which idiom to use instead. Rewrite each function
body using that idiom. **Don't change the function names or signatures** — the
tests call them directly by name.

## Run it
```bash
# from the repo root, one-time setup:
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

cd day01-pythonic-data-structures
pytest -v
```
All 3 tests fail right now (or rather, they pass against the naive version too —
open `starter.py` to see why this is still worth doing: the naive version *works*,
it's just not how you want to be writing Python by the end of this). Once you've
rewritten each function, rerun `pytest -v` and re-read your diff against
`solution.py` to compare style, not just correctness.

## Common pitfalls
- A comprehension that's doing too much (nested conditionals, side effects) —
  split it back into a loop, or a helper function called from inside the
  comprehension.
- `zip()` stopping early is a silent bug source if you *expect* equal-length
  inputs and one is short by a typo elsewhere in your code — worth a mental note,
  not something to fix today.
- Dict comprehensions silently overwrite on duplicate keys (last one wins) — fine
  most of the time, but know it's happening.

## Stretch goal (optional)
Rewrite `get_even_squares` again, but as a **generator expression**
(`(x*x for x in nums if x % 2 == 0)` — parens instead of brackets) instead of a
list comprehension. Notice it doesn't build the whole list in memory up front.
This is the seed of Day 6 (generators).

## Further reading
- Official tutorial section this all comes from: https://docs.python.org/3/tutorial/datastructures.html
- PEP 8 (style guide — worth skimming once, ever): https://peps.python.org/pep-0008/
