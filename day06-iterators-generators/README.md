# Day 6 — Iterators & Generators

## Why this matters
Every function you wrote on Day 1 that builds a list computes the *entire*
result before returning anything. That's fine for small data, but if you're
processing a huge file, an infinite stream, or something expensive to compute
per item, building the whole list up front wastes memory and time you don't
need to spend yet. A generator produces values *one at a time, on demand* —
you get the first result immediately instead of waiting for all of them.

## Where you'll actually use this
- **ML data loading**: PyTorch's `DataLoader` and most data pipelines are
  built on generators/iterators specifically so you never load an entire
  dataset into RAM at once — this is not optional at any real scale.
- **Processing large files or log streams**: reading a multi-GB log file line
  by line with a generator instead of `.readlines()` (which loads it all).
- **Interviews**: "make this lazy" or "what if this list were infinite" is a
  common follow-up question after any list-building exercise — this is
  exactly what today trains you to answer.

## Concepts & syntax

### `yield` and generator functions
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```
Calling `count_up_to(5)` does **not** run the function body — it instantly
returns a generator object. The body only runs when you iterate it (`for x in
count_up_to(5)`, or `next(gen)`), and it runs *up to* the next `yield`, pauses
there, and resumes exactly where it left off next time you ask for a value.
**When to use it:** any time you're producing a sequence of values you don't
need all at once. **When not to:** if you need to iterate the same data
multiple times or need random access (`data[5]`) — a generator is single-use
and forward-only; use a list if you need those things.
Docs: https://docs.python.org/3/tutorial/classes.html#generators

### Generator expressions
```python
squares = (x * x for x in range(1000000))   # parens, not brackets
```
The lazy sibling of a list comprehension — same syntax, but doesn't build
anything until you iterate it.
Docs: https://docs.python.org/3/reference/expressions.html#generator-expressions

### `itertools.islice`
```python
import itertools
first_five = list(itertools.islice(some_generator, 5))
```
Takes the first N items from *any* iterable — including an infinite one —
without ever asking it for more than that. This is how you safely "peek" at
a generator.
Docs: https://docs.python.org/3/library/itertools.html#itertools.islice

### `itertools.groupby`
```python
import itertools
for key, group in itertools.groupby([1, 1, 2, 2, 2, 3]):
    print(key, list(group))
# 1 [1, 1]
# 2 [2, 2, 2]
# 3 [3]
```
Groups **consecutive** equal elements (it does *not* group all matching
elements across the whole list — only runs — which trips people up the first
time). `group` is itself a generator, so wrap it in `list(...)` if you need to
use it more than once or need its length.
Docs: https://docs.python.org/3/library/itertools.html#itertools.groupby

## The task
Open `starter.py`. Three functions, each written the "eager" way:
1. `read_large_numbers(n)` — rewrite as a generator function using `yield`
   instead of building a list.
2. `first_n_over_threshold(numbers, threshold, n)` — rewrite using a generator
   expression + `itertools.islice` so it works correctly (and efficiently)
   even if `numbers` is an infinite iterable.
3. `group_consecutive_duplicates(items)` — rewrite using `itertools.groupby`.

## Run it
```bash
cd day06-iterators-generators
pytest -v
```
Notice: the value-correctness tests already pass against the naive
`read_large_numbers` — but `test_read_large_numbers_is_a_generator` fails,
because a list and a generator behave differently even when they produce the
same values. That test is the one proving you actually changed the
*mechanism*, not just kept the same output.

## Common pitfalls
- A generator can only be iterated **once**. If you do
  `list(gen); list(gen)` the second call returns `[]` — it's already
  exhausted. If you need to reuse it, convert to a list deliberately, or call
  the generator function again to get a fresh one.
- `itertools.groupby` only groups *consecutive* runs — `groupby([1,2,1])`
  produces three separate groups of size 1 each, not one group of two 1s.
  Sort first if you actually want "group all matching items regardless of
  position."
- Forgetting that `group` inside `groupby` is itself a lazy iterator — if you
  don't consume it (e.g. with `list(group)`) before moving to the next
  iteration of the outer loop, its contents become unreliable.

## Stretch goal (optional)
Write a generator function `fibonacci()` that yields the Fibonacci sequence
**forever** (no upper bound — just `while True: yield ...`). Then use
`itertools.islice(fibonacci(), 10)` to safely get the first 10 values. This is
the clearest possible demonstration of why laziness matters: the function
itself has no concept of "when to stop."

## Further reading
- `itertools` full recipe list (extremely useful reference):
  https://docs.python.org/3/library/itertools.html
- Python's own generator tutorial section:
  https://docs.python.org/3/tutorial/classes.html#generators
