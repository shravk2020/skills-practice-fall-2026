# Day 5 — Errors & Context Managers

## Why this matters
Two related skills: (1) raising *your own* exception types instead of letting
generic errors bubble up with no context, and (2) guaranteeing cleanup happens
even when something goes wrong — a file gets closed, a connection gets
released, a lock gets freed — no matter how the code inside a block exits.

## Where you'll actually use this
- **FastAPI error handling (Week 3)**: you'll raise `HTTPException` with
  specific status codes constantly — custom exceptions are the same idea,
  just before you've wired them to HTTP responses.
- **Database connections (Week 5)**: `with db.get_connection() as conn:` is a
  context manager — it's exactly this repo's `scripts/db.py` pattern, and
  it's how you guarantee a connection gets closed even if a query throws.
- **Interviews**: raising a specific, well-named exception instead of a bare
  `Exception` or `ValueError` for everything is a clear signal of code
  maturity — reviewers notice this immediately.

## Concepts & syntax

### Custom exceptions
```python
class NegativeValueError(Exception):
    pass

def require_non_negative(n):
    if n < 0:
        raise NegativeValueError(f"expected non-negative, got {n}")
    return n
```
Subclassing `Exception` gives you a named, specific error type that callers
can catch selectively (`except NegativeValueError:`) instead of catching
*everything* with a bare `except Exception:` and having to guess what went
wrong. **When to use it:** whenever "something went wrong" needs to be more
specific than Python's built-in exceptions (`ValueError`, `KeyError`, etc.)
capture. **When not to:** if a built-in exception already says exactly what
happened (e.g. `ValueError` for bad input) — don't invent a new type just for
the sake of it.
Docs: https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions

### `try` / `except` / `else` / `finally`
```python
try:
    risky()
except ValueError as e:
    print(f"handled: {e}")
else:
    print("only runs if no exception was raised")
finally:
    print("always runs, exception or not")
```
`finally` is the key one for today — it runs no matter what, including if the
exception isn't caught at all and propagates past this block.
Docs: https://docs.python.org/3/tutorial/errors.html#handling-exceptions

### Context managers (the `with` statement)
```python
with open("file.txt") as f:
    data = f.read()
# f is guaranteed to be closed here, even if .read() raised an exception
```
You've used this dozens of times with `open()`. Today you build your own.

### Writing a context manager as a class
```python
class MyContextManager:
    def __enter__(self):
        # runs when entering the `with` block
        return self   # whatever this returns becomes the `as x` value

    def __exit__(self, exc_type, exc_value, traceback):
        # runs when leaving the block, exception or not
        # exc_type is None if no exception occurred
        # return True to SUPPRESS the exception (stop it from propagating)
        # return False (or None) to let it propagate normally
        ...
```
`__exit__`'s three arguments tell you exactly what exception (if any) is in
flight. This is the mechanism `contextlib.suppress()` and your `starter.py`
class both use.
Docs: https://docs.python.org/3/reference/datamodel.html#context-managers

## The task
Open `starter.py`. Implement:
1. `require_non_negative(n)` — raises `NegativeValueError` if `n < 0`,
   otherwise returns `n` unchanged.
2. `suppress_and_log` — a context manager class. Takes one or more exception
   *classes* as constructor arguments (e.g. `suppress_and_log(ValueError, KeyError)`).
   If the code inside the `with` block raises one of those exception types,
   print `f"Suppressed: {exception}"` and prevent it from propagating further.
   If it raises a *different* exception type (not in the list), let it
   propagate normally — don't suppress it.

## Run it
```bash
cd day05-errors-context-managers
pytest -v
```

## Common pitfalls
- `__exit__` must check `exc_type` against the exceptions you were given using
  something like `issubclass(exc_type, self.exceptions)` — comparing types
  directly with `==` will miss subclasses.
- Returning `None` from `__exit__` (i.e., no explicit `return`) means "don't
  suppress" — it's easy to think "no return = suppress" by accident. You must
  explicitly `return True` to suppress.
- `exc_type` is `None` when the block exits normally (no exception) —
  `__exit__` still runs in that case, so guard against calling
  `issubclass(None, ...)`, which raises a `TypeError`.

## Stretch goal (optional)
Rewrite `suppress_and_log` using `@contextlib.contextmanager` and a generator
function with `yield` instead of a class with `__enter__`/`__exit__`. Same
behavior, much less boilerplate — this is the version you'd actually write in
real code once you understand what it's doing underneath.
Docs: https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager

## Further reading
- `contextlib` module (lots of ready-made context manager helpers):
  https://docs.python.org/3/library/contextlib.html
- Full exceptions tutorial: https://docs.python.org/3/tutorial/errors.html
