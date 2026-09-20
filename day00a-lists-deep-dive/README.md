# Day 0a — Lists, Deep Dive

## Why this matters
Day 1 jumped straight to list *comprehensions* — the shortcut. This day is
the thing the shortcut is a shortcut *for*: what a list actually is, every
method it has, how slicing really works, and the mutability gotchas that
cause real bugs (including a classic one that shows up in actual interviews).
Skipping this and going straight to comprehensions is like learning chord
shapes before you know what a note is.

## Where you'll actually use this
- **Literally everywhere** — lists are the single most-used data structure in
  Python. Every day for the rest of this plan uses them.
- **The mutable-default-argument bug** (covered below) is one of the most
  common real bugs in production Python code, and a very common "gotcha"
  interview question.
- **Slicing** is how you'll do pagination, "last N items," windowing, and
  reversing — all things you'll do constantly in real backend code.

## The full method reference
This is the complete list of methods every `list` has. You won't use all of
them today, but you should know they exist and roughly when you'd reach for
each one.

| Method | What it does | Mutates in place? |
|---|---|---|
| `.append(x)` | add `x` to the end | yes |
| `.extend(iterable)` | add every item from `iterable` to the end | yes |
| `.insert(i, x)` | insert `x` at index `i` | yes |
| `.remove(x)` | remove the **first** occurrence of `x` (raises `ValueError` if not found) | yes |
| `.pop(i=-1)` | remove **and return** the item at index `i` (default: last item) | yes |
| `.clear()` | remove everything | yes |
| `.index(x)` | return the index of the first occurrence of `x` (raises `ValueError` if not found) | no |
| `.count(x)` | how many times `x` appears | no |
| `.sort(key=None, reverse=False)` | sort **in place** | yes |
| `.reverse()` | reverse **in place** | yes |
| `.copy()` | return a shallow copy (same as `items[:]`) | no |

And the operators/builtins that go with lists:

| Syntax | What it does |
|---|---|
| `a + b` | a **new** list, `a`'s items then `b`'s items (doesn't mutate either) |
| `a * 3` | a **new** list, `a`'s items repeated 3 times |
| `x in items` | membership test — `True`/`False` |
| `len(items)` | item count |
| `items[i]` | index — negative `i` counts from the end (`items[-1]` is the last item) |
| `items[start:stop:step]` | slicing — see below |
| `sorted(items, key=..., reverse=...)` | like `.sort()` but returns a **new** list, doesn't mutate |
| `del items[i]` | remove the item at index `i` without returning it |

## Concepts in depth

### Slicing, fully
```python
items = [10, 20, 30, 40, 50]
items[1:3]     # [20, 30]      -- index 1 up to (not including) index 3
items[:2]      # [10, 20]      -- from the start
items[3:]      # [40, 50]      -- to the end
items[-2:]     # [40, 50]      -- last 2 items
items[::2]     # [10, 30, 50]  -- every 2nd item
items[::-1]    # [50, 40, 30, 20, 10]  -- reversed
```
A slice never raises an `IndexError` even if the range goes out of bounds
(`items[1:100]` just returns what exists) — this is different from
`items[100]`, which does raise.
Docs: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

### `.sort()` vs `sorted()`
```python
items.sort()              # mutates items, returns None
new_list = sorted(items)  # leaves items alone, returns a new sorted list
```
Both take `key=` (a function applied to each item to determine sort order)
and `reverse=True`. **When to use which:** `.sort()` if you don't need the
original order anymore; `sorted()` if you do, or if you're sorting something
that isn't a list to begin with (`sorted()` works on any iterable).
Docs: https://docs.python.org/3/howto/sorting.html

### The mutable default argument bug
```python
def add_item(item, items=[]):     # DANGER
    items.append(item)
    return items

add_item("a")   # ['a']
add_item("b")   # ['a', 'b']  <- surprise! Not a fresh list.
```
Default argument values are evaluated **once**, when the function is
defined — not once per call. A mutable default (`[]`, `{}`) gets shared and
mutated across every call that doesn't pass its own value. The fix:
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```
This is a real, extremely common bug — know it cold.
Docs: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
(see the warning box on that page)

### Aliasing vs. copying
```python
a = [1, 2, 3]
b = a            # b is the SAME list as a, not a copy
b.append(4)
a                # [1, 2, 3, 4]  <- a changed too!

c = a.copy()     # c is a NEW list with the same items
c.append(5)
a                # [1, 2, 3, 4]  <- unaffected
```
Assignment (`=`) never copies a list — it just gives a second name to the
same object. Use `.copy()` (or `items[:]`) when you actually need an
independent list.

## The task
Open `starter.py`. Implement each function using the specific method named
in its docstring — the point today is deliberately using the *named* tool,
not whichever approach happens to work.

## Run it
```bash
cd day00a-lists-deep-dive
pytest -v
```

## Common pitfalls
- `.remove(x)` removes only the *first* match — if you need to remove every
  occurrence of a value, you need a loop or a comprehension, not a single
  `.remove()` call.
- `.pop()` with no argument removes the **last** item, not the first —
  `.pop(0)` removes the first (but is slower on large lists, since every
  remaining item has to shift over).
- `.sort()` returns `None` — `items = items.sort()` is a very common mistake
  that silently sets `items` to `None`.

## Stretch goal (optional)
Write a function that removes **all** occurrences of a value from a list
without building a new list (i.e. don't just `return [x for x in items if x
!= value]`) — you have to actually mutate `items` in place using `.remove()`
in a loop. Notice the trap: removing items while iterating forward over the
same list skips elements. Figure out why, and fix it (hint: iterate over a
`.copy()`, or iterate backwards by index).

## Further reading
- Full sequence operations reference: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
- Python's own sorting how-to: https://docs.python.org/3/howto/sorting.html
