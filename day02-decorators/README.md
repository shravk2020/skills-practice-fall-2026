# Day 2 — Functions, Closures, Decorators

## Why this matters
A decorator wraps one function with another, adding behavior (timing, retrying,
logging, auth checks) without touching the original function's code. You've
already *used* decorators without necessarily building one — `@app.get("/status")`
in FastAPI, `@pytest.mark.parametrize`, `@property` are all decorators. Today
you build two from scratch so `@app.get(...)` stops being magic syntax and
becomes something you actually understand.

## Where you'll actually use this
- **FastAPI itself is built on decorators** (`@app.get`, `@app.post`) — Week 3
  will make a lot more sense after today.
- **Logging/timing production code**: wrapping a slow function with `@timer` to
  find bottlenecks is one of the most common real-world uses.
- **Retry logic for flaky network calls**: any code that calls an external API
  (Day 14's httpx work, or any real backend job) needs retry logic — this is
  the exact pattern, just with `time.sleep` between attempts in production.
- **Interviews**: "write a decorator" is an extremely common backend interview
  question because it tests whether you understand functions as first-class
  values, not just syntax memorization.

## Concepts & syntax

### Functions are values
```python
def add(a, b):
    return a + b

my_func = add          # no parens = don't call it, just reference it
my_func(2, 3)           # 5
```
This is the foundation everything else today builds on: a function can be
passed around, stored in a variable, passed as an argument, and returned from
another function — just like an int or a string.
Docs: https://docs.python.org/3/reference/compound_stmts.html#function-definitions

### Closures
```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor       # `factor` is "closed over" from the outer scope
    return multiply

times3 = make_multiplier(3)
times3(10)   # 30
```
The inner function remembers `factor` even after `make_multiplier` has returned.
This is exactly how a decorator "remembers" the function it's wrapping.
**When to use it:** any time you need to generate a customized function on the
fly (like `retry(times=3)` below). **When not to:** if you're closing over a
mutable variable that changes later, you can get surprising bugs — know that
closures capture the *variable*, not a frozen copy of its value at that moment.

### `*args`, `**kwargs`
```python
def call_and_print(func, *args, **kwargs):
    result = func(*args, **kwargs)
    print(result)
```
`*args` collects any number of positional arguments into a tuple; `**kwargs`
collects any number of keyword arguments into a dict. A decorator needs these
because it doesn't know in advance what arguments the function it's wrapping
will be called with.
Docs: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

### The decorator pattern
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # ...do something before...
        result = func(*args, **kwargs)
        # ...do something after...
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"hello {name}"

# equivalent to: greet = my_decorator(greet)
```
`@my_decorator` above a function definition is just syntax sugar for
`greet = my_decorator(greet)`. That's the whole trick.
Docs: https://docs.python.org/3/glossary.html#term-decorator

### `functools.wraps`
```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
Without this, `greet.__name__` becomes `"wrapper"` after decorating, which
breaks debugging, docs, and introspection tools. **Always** use
`functools.wraps(func)` on the inner function of a real decorator — treat it
as non-optional boilerplate, not a nice-to-have.
Docs: https://docs.python.org/3/library/functools.html#functools.wraps

### Decorators that take arguments (decorator factories)
```python
def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator

@retry(times=5)
def flaky_call():
    ...
```
Three layers deep: `retry(times=5)` runs first and returns `decorator`, which
then gets applied to `flaky_call`. This is the exact shape of
`@pytest.mark.parametrize(...)` and FastAPI's `@app.get("/path")`.

## The task
Open `starter.py`. Implement:
1. `timer` — a plain decorator (no arguments) that prints how long the wrapped
   function took to run (use `time.perf_counter()` before and after), then
   returns the function's normal return value, unmodified.
2. `retry(times=3)` — a decorator factory. The wrapped function should be called;
   if it raises an exception, retry it, up to `times` total attempts. If it
   still fails after the last attempt, let the exception propagate normally
   (don't swallow it).

## Run it
```bash
cd day02-decorators
pytest -v
```

## Common pitfalls
- Forgetting `functools.wraps` — tests here won't catch it, but it's a real bug
  in production code. Add it anyway; make it a habit now.
- In `retry`, an off-by-one on the attempt count is the easiest mistake —
  "3 times" should mean 3 total calls maximum, not 3 retries *after* the first
  call (4 total). Read the test cases in `test_starter.py` carefully; they
  pin down exactly which behavior is expected.
- `wrapper` must return `func(*args, **kwargs)`'s result — a decorator that
  forgets to `return` silently turns every wrapped function into one that
  always returns `None`. This is a very common real bug.

## Stretch goal (optional)
Add a `min_delay` parameter to `retry` that calls `time.sleep(min_delay)`
between attempts (default `0`) — this is what makes retry logic actually usable
against a real flaky network call instead of just a test.

## Further reading
- Real Python's decorator primer (much longer, good if this feels shaky):
  https://realpython.com/primer-on-python-decorators/
- `functools` docs (has more built-in decorators worth knowing, like `lru_cache`):
  https://docs.python.org/3/library/functools.html
