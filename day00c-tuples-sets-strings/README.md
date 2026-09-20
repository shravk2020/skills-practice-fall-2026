# Day 0c — Tuples, Sets & Strings

## Why this matters
Three more data types you've been using casually without their full toolkit:
tuples (immutable, fixed-shape data), sets (fast membership + real math-style
set operations), and strings (which have far more methods than `.split()`
and `.join()`). All three show up constantly in cleaning and reshaping real
data — which is most of what a backend or ML script actually spends its time
doing.

## Where you'll actually use this
- **Sets** are how you deduplicate, and how you answer "what do these two
  groups have in common / what's different" — extremely common in data
  processing and in interview questions.
- **String methods** are what you use on every piece of user input or file
  content before it's clean enough to actually work with — this is a huge
  fraction of real data-cleaning code.
- **Tuples** show up as dict keys (lists can't be dict keys — tuples can),
  function return values (`return min_val, max_val`), and anywhere data
  shouldn't change after creation.

## The full method reference

### Sets
| Method / operator | What it does |
|---|---|
| `s.add(x)` | add `x` |
| `s.remove(x)` | remove `x` (raises `KeyError` if not present) |
| `s.discard(x)` | remove `x` if present, do nothing if not (never raises) |
| `s.update(iterable)` | add every item from `iterable` |
| `a \| b` | union — everything in either | 
| `a & b` | intersection — only what's in both |
| `a - b` | difference — in `a` but not `b` |
| `a ^ b` | symmetric difference — in exactly one of the two, not both |
| `a.issubset(b)` | is every item of `a` also in `b`? |
| `a.issuperset(b)` | does `a` contain every item of `b`? |

Sets are unordered and only hold **unique, hashable** values (no duplicates,
no lists/dicts inside a set). Membership testing (`x in my_set`) is O(1) —
much faster than `x in my_list` on a large list, which is O(n).
Docs: https://docs.python.org/3/library/stdtypes.html#set

### Strings (the most common methods)
| Method | What it does |
|---|---|
| `.split(sep=None)` | split into a list on `sep` (or any whitespace if omitted) |
| `.rsplit(sep, maxsplit)` | split from the right, at most `maxsplit` times |
| `.join(iterable)` | opposite of split — `"-".join(["a","b"])` -> `"a-b"` |
| `.strip()` / `.lstrip()` / `.rstrip()` | remove whitespace (or given chars) from both/left/right ends |
| `.replace(old, new)` | replace all occurrences |
| `.upper()` / `.lower()` / `.title()` | case conversion |
| `.startswith(x)` / `.endswith(x)` | prefix/suffix check |
| `.find(x)` | index of first occurrence, or `-1` if not found (unlike `.index()`, never raises) |
| `.isdigit()` / `.isalpha()` / `.isalnum()` | character-class checks |
| `f"{value}"` | f-strings — the modern way to build strings with embedded values |

Docs: https://docs.python.org/3/library/stdtypes.html#string-methods

### Tuples
```python
point = (3, 4)
x, y = point              # unpacking
first, *rest = [1, 2, 3, 4]    # first = 1, rest = [2, 3, 4]
*init, last = [1, 2, 3, 4]     # init = [1, 2, 3], last = 4
```
Tuples are immutable — no `.append()`, no `.remove()`. What they *do* have:
`.count(x)` and `.index(x)`, same meaning as on lists. Their real value is
signaling "this shouldn't change" and being usable as dict keys
(`{(0, 0): "origin"}`) where a list couldn't be.
Docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

## The task
Open `starter.py`. Implement each function using the method/operator named
in its docstring.

## Run it
```bash
cd day00c-tuples-sets-strings
pytest -v
```

## Common pitfalls
- `.remove()` on a set raises `KeyError` if the item isn't there; `.discard()`
  doesn't. Use `.discard()` when "it might not be there" is a normal case,
  `.remove()` when its absence would actually be a bug.
- `"a,b,,c".split(",")` gives `['a', 'b', '', 'c']` — an empty string between
  two separators becomes an empty-string element, not nothing. This trips
  people up parsing real-world messy data (like a CSV with an empty field).
- A single-element tuple needs a trailing comma: `(1)` is just the int `1`
  in parentheses; `(1,)` is a tuple. Easy to forget.

## Stretch goal (optional)
Write `most_common_word(text)` that lowercases the text, splits it into
words, strips basic punctuation off each word (`.strip(".,!?")`), and
returns the single most frequent word (you can use `collections.Counter`
here, or the `.get()`-counting pattern from Day 0b).

## Further reading
- All string methods, the full list: https://docs.python.org/3/library/stdtypes.html#string-methods
- Set types reference: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
