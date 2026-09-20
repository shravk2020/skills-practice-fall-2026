# Day 0b — Dictionaries, Deep Dive

## Why this matters
Dicts are how you model "a thing with named fields" and "a lookup table" —
two of the most common shapes of data in any real program. Knowing the full
method set means you stop writing `if key in d: x = d[key] else: x = default`
by hand when `.get(key, default)` does it in one line, and stop overwriting
data by accident when `.setdefault()` or `.update()` is what you actually
wanted.

## Where you'll actually use this
- **Every JSON API response or request body is a dict** (or a list of
  dicts) once it hits your Python code — FastAPI's Pydantic models are built
  on top of this same idea.
- **Counting/grouping patterns** (word frequency, grouping records by a
  field) are one of the most common real interview and real-job tasks, and
  they're built entirely out of `.get()`/`.setdefault()`.
- **Config merging** (defaults + user overrides) is a dict-merging pattern
  you'll use in almost every real project, including this one's own `.env`
  handling later.

## The full method reference

| Method | What it does |
|---|---|
| `d.get(key, default=None)` | look up `key`; return `default` (not a `KeyError`) if missing |
| `d.setdefault(key, default)` | if `key` exists, return its value; otherwise **set** `d[key] = default` and return it |
| `d.update(other)` | merge `other` (a dict, or an iterable of pairs) into `d`, overwriting existing keys |
| `d.pop(key, default=...)` | remove `key` and return its value; return `default` instead of raising if missing (raises `KeyError` if no default given and key is missing) |
| `d.popitem()` | remove and return the **last-inserted** `(key, value)` pair |
| `d.keys()` | a view of all keys |
| `d.values()` | a view of all values |
| `d.items()` | a view of all `(key, value)` pairs |
| `d.copy()` | a shallow copy |
| `d.clear()` | remove everything |
| `dict.fromkeys(iterable, value)` | build a new dict with every item in `iterable` as a key, all mapped to the same `value` |

And the operators/syntax that go with dicts:

| Syntax | What it does |
|---|---|
| `key in d` | membership test — checks **keys**, not values |
| `del d[key]` | remove `key` (raises `KeyError` if missing) |
| `d[key]` | direct lookup — raises `KeyError` if missing (unlike `.get()`) |
| `d1 \| d2` | a **new** dict: `d1`'s items, then `d2`'s items merged in on top (Python 3.9+) |
| `d1 \|= d2` | merge `d2` into `d1` in place (same result as `d1.update(d2)`) |
| `{k: v for k, v in ...}` | dict comprehension (you used this Day 1) |

## Concepts in depth

### `.get()` vs `d[key]` vs `.setdefault()`
```python
d = {"a": 1}
d["b"]                    # KeyError!
d.get("b")                 # None
d.get("b", 0)               # 0 -- doesn't add "b" to d
d.setdefault("b", 0)        # 0 -- AND now d == {"a": 1, "b": 0}
```
Use `d[key]` when the key is *supposed* to be there and its absence is a bug
you want to know about loudly. Use `.get()` for "give me this or a fallback,
and don't change the dict." Use `.setdefault()` specifically when you want
"give me this, and if it wasn't there, remember this default for next time"
— it's the classic building block for grouping/counting patterns:
```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1   # or: counts.setdefault(word, 0); counts[word] += 1
```
Docs: https://docs.python.org/3/library/stdtypes.html#dict

### Merging dicts
```python
defaults = {"theme": "light", "font_size": 12}
overrides = {"font_size": 14}

merged = defaults | overrides      # {"theme": "light", "font_size": 14}
# equivalent, older style:
merged = {**defaults, **overrides}
```
**When to use `|` vs `.update()`:** `|` creates a new dict (doesn't touch
either original) — prefer it when you don't want to mutate `defaults`.
`.update()` mutates in place — use it when you specifically want to change
an existing dict, e.g. accumulating into one dict across a loop.
Docs: https://docs.python.org/3/library/stdtypes.html#dict (see "union")

### Iterating
```python
for key in d:                 # same as d.keys()
    ...
for value in d.values():
    ...
for key, value in d.items():  # by far the most common pattern
    ...
```
`.keys()`, `.values()`, `.items()` return *views*, not lists — they stay in
sync with the dict live, and are memory-efficient (closer to Day 6's
generators than to a built list), but you can't index into them directly
(`d.keys()[0]` doesn't work — wrap in `list(...)` first if you need that).

## The task
Open `starter.py`. Implement each function using the method named in its
docstring.

## Run it
```bash
cd day00b-dicts-deep-dive
pytest -v
```

## Common pitfalls
- `d[key]` on a missing key crashes your whole program if you're not
  expecting it — in real code, an uncaught `KeyError` from a typo'd
  dictionary key is a very common source of 500 errors in a backend.
- Dicts in Python 3.7+ preserve **insertion order** (this is guaranteed
  behavior, not an implementation detail) — `.popitem()` specifically
  removes the *last* inserted item because of this.
- `key in d` checks keys only. If you actually need to check whether a
  *value* exists anywhere in the dict, you need `value in d.values()`,
  which is O(n) (a full scan) — very different from the O(1) key lookup.

## Stretch goal (optional)
Write `group_by_first_letter(words)` that returns a dict mapping each
distinct first letter to a list of all words starting with it, e.g.
`["apple", "avocado", "banana"] -> {"a": ["apple", "avocado"], "b": ["banana"]}`.
Use `.setdefault(letter, []).append(word)` — this exact pattern (setdefault
with a mutable default) is one of the most useful one-liners in everyday
Python.

## Further reading
- Full dict reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
- Python's own dict how-to section of the tutorial:
  https://docs.python.org/3/tutorial/datastructures.html#dictionaries
