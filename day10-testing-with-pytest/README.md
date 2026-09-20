# Day 10 — Testing With Pytest (Fixtures, Parametrize, Mocking)

## Why this matters
So far, every test file in this lab has quietly used pytest's basics
(`def test_...`, plain `assert`). Today makes three more advanced pytest
features explicit: **fixtures** (reusable setup/teardown), **parametrize**
(running the same test against many inputs without copy-pasting it), and
**mocking** (faking a dependency you don't want your test to actually call,
like a network request). All three appear constantly in every test file from
Week 3 onward.

## Where you'll actually use this
- **Testing FastAPI (Day 15)**: you'll mock outbound httpx calls so your test
  suite doesn't depend on a real network connection or a third-party API
  being up.
- **Any test involving external state** (a database, an API, the current
  time, a random number) — you mock it so your tests are fast, reliable, and
  don't have side effects.
- **Interviews**: being asked "how would you test this without hitting the
  real API" is extremely common for backend roles — mocking is *the* answer.

## Concepts & syntax

### Fixtures
```python
import pytest

@pytest.fixture
def sample_data():
    return {"a": 1, "b": 2}

def test_something(sample_data):
    assert sample_data["a"] == 1
```
A fixture is a function pytest runs *before* a test that uses it, and passes
its return value in as an argument matching the fixture's name. Use fixtures
for setup you'd otherwise repeat at the top of every test (test data,
temp files — you already used pytest's built-in `tmp_path` fixture on Day 7).
A fixture using `yield` instead of `return` can also run cleanup code after
the test finishes (whatever comes after the `yield`).
Docs: https://docs.python.org/3/library/unittest.mock.html (mock reference)
and https://docs.pytest.org/en/stable/how-to/fixtures.html (fixtures)

### `@pytest.mark.parametrize`
```python
@pytest.mark.parametrize("input_val, expected", [
    (1, "odd"),
    (2, "even"),
    (0, "even"),
])
def test_parity(input_val, expected):
    assert classify(input_val) == expected
```
Runs the same test function once per row, each showing up as its own
separate result in the test output. **When to use it:** any time you'd
otherwise write 3+ near-identical test functions that only differ in their
input/expected values.
Docs: https://docs.pytest.org/en/stable/how-to/parametrize.html

### Mocking with `unittest.mock.patch`
```python
from unittest.mock import patch

def test_something():
    with patch("mymodule.some_function") as mock_func:
        mock_func.return_value = 42
        result = mymodule.caller_that_uses_some_function()
        assert result == 42 + 1
        mock_func.assert_called_once()
```
`patch("mymodule.some_function")` temporarily replaces that function (inside
the module where it's *used*, not necessarily where it's defined — this
trips everyone up at least once) with a fake object for the duration of the
`with` block. You control what it returns (`.return_value`) and can assert
how it was called (`.assert_called_once_with(...)`).
Docs: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

### Combining a fixture with mocking
```python
@pytest.fixture
def mock_temp():
    with patch("starter.fetch_temperature") as mock:
        yield mock
```
This is today's exact pattern: a fixture that sets up the patch once, `yield`s
the mock object so every test that needs it can configure its return value,
and automatically un-patches when the `with` block ends after the test.

## The task
Open `starter.py`. There's a `fetch_temperature(city)` function that's
intentionally unimplemented (it raises `NotImplementedError`) — pretend it
calls a real weather API. Implement `describe_weather(city)`, which:
1. Calls `fetch_temperature(city)` to get a Fahrenheit temperature.
2. Returns a message based on the temperature:
   - `< 32`: `"{city}: freezing ({temp}°F)"`
   - `32-59`: `"{city}: cold ({temp}°F)"`
   - `60-79`: `"{city}: mild ({temp}°F)"`
   - `>= 80`: `"{city}: hot ({temp}°F)"`

You won't touch the test file, but read it closely — it's the actual lesson
today, showing the fixture/parametrize/mock pattern in action against the
function you're about to write.

## Run it
```bash
cd day10-testing-with-pytest
pytest -v
```

## Common pitfalls
- Patch the name **where it's looked up**, not where it's defined. Here
  that's `"starter.fetch_temperature"` (because `describe_weather` looks it
  up inside the `starter` module), not the string `"fetch_temperature"`
  alone.
- Forgetting `yield` in a fixture that uses `patch(...)` as a context
  manager — using `return` instead means the patch gets undone before your
  test even runs, and you'd be testing against the real (unimplemented)
  function.
- Parametrize test IDs can get confusing with many cases — pytest shows you
  exactly which parameter set failed in its output; read that carefully
  rather than guessing.

## Stretch goal (optional)
Add a new parametrized case for `temp == 32` and `temp == 60` (the exact
boundary values) to make sure your `if`/`elif` conditions use the right
comparison operators (`<` vs `<=`) at the edges — boundary values are where
off-by-one bugs in threshold logic like this actually hide.

## Further reading
- pytest's fixture guide (the best single doc for this):
  https://docs.pytest.org/en/stable/how-to/fixtures.html
- `unittest.mock` full reference: https://docs.python.org/3/library/unittest.mock.html
