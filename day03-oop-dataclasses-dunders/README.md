# Day 3 — OOP Done Right

## Why this matters
A "class" isn't just a way to group data — it's a way to make invalid states
hard to represent and give your objects sensible default behavior (printing,
equality, computed values) for free. Today you build one class manually so you
understand what's actually happening before you ever use `@dataclass` as a
shortcut for it.

## Where you'll actually use this
- **Pydantic models (Week 3) are classes** with validation and computed fields —
  today's `@property` work is a direct preview of that.
- **ORMs like SQLAlchemy/SQLModel (Day 24)** map database rows to Python
  classes — understanding `__init__`, `__eq__`, and `__repr__` is exactly what
  makes those tools make sense instead of feeling like magic.
- **Interviews**: "implement a class with X behavior" is standard, and graders
  specifically check for `__repr__`/`__eq__` because forgetting them is the
  #1 sign of someone who's only ever used classes, never designed one.

## Concepts & syntax

### `__init__`
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```
The constructor. `self` is the instance being created — every method on a class
takes `self` as its first parameter so it can read/write that instance's data.
Docs: https://docs.python.org/3/tutorial/classes.html

### `@property`
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```
Lets you call `rect.area` like an attribute (`rect.area`, no parens) even
though it's computed from a method. **When to use it:** any value that's
*derived* from other attributes and shouldn't be stored/settable directly
(area from width/height; full_name from first/last). **When not to:** if
computing it is expensive (e.g. a database query) — a property that silently
runs a slow operation on every access is a common footgun; a regular method
makes the cost visible at the call site.
Docs: https://docs.python.org/3/library/functions.html#property

### `__repr__`
```python
def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
```
Controls what you see when you `print(obj)` or look at it in a debugger/REPL.
Without it, Python shows something useless like `<Rectangle object at 0x...>`.
**Convention:** `__repr__` should look like valid Python that could recreate
the object.
Docs: https://docs.python.org/3/reference/datamodel.html#object.__repr__

### `__eq__`
```python
def __eq__(self, other):
    return self.width == other.width and self.height == other.height
```
Without this, `Rectangle(3, 4) == Rectangle(3, 4)` is `False` — by default,
Python compares *identity* (are these literally the same object in memory?),
not *value*. Defining `__eq__` tells Python how to compare values instead.
Docs: https://docs.python.org/3/reference/datamodel.html#object.__eq__

### `@dataclass` (the shortcut — mentioned, not required today)
```python
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float
```
This one decorator auto-generates `__init__`, `__repr__`, and `__eq__` for you.
You're building it by hand today specifically so `@dataclass` stops being a
black box — from Day 4 onward, feel free to reach for it in your own code.
Docs: https://docs.python.org/3/library/dataclasses.html

## The task
Open `starter.py`. Implement the `Rectangle` class with:
- `__init__(self, width, height)`
- a read-only `area` property (`width * height`)
- `__repr__` returning exactly `"Rectangle(width=3, height=4)"` style (no
  decimal point if the input was an int — just use `f"...{self.width}..."`,
  don't force formatting)
- `__eq__` comparing another `Rectangle`'s width and height

## Run it
```bash
cd day03-oop-dataclasses-dunders
pytest -v
```

## Common pitfalls
- Making `area` a regular attribute set in `__init__` instead of a
  `@property` — it'll pass a naive equality check but fails the
  "read-only" test, and more importantly, it'll go stale if `width`/`height`
  change after construction. A property recomputes every time, so it can
  never be wrong.
- `__eq__` that crashes if `other` isn't a `Rectangle` (e.g. comparing to a
  string) — real-world code should either return `NotImplemented` for
  unrecognized types or check `isinstance` first. The tests here only compare
  two `Rectangle`s, but it's worth knowing this edge case exists.

## Stretch goal (optional)
Add a `__lt__` method so `Rectangle`s can be sorted by area
(`sorted([r1, r2, r3])`). This is the same idea as `__eq__` — you're teaching
Python how to compare your custom objects.

## Further reading
- Data model reference (all the dunder methods in one place):
  https://docs.python.org/3/reference/datamodel.html#special-method-names
- Real Python on dataclasses (good once you're ready to stop doing this by hand):
  https://realpython.com/python-data-classes/
