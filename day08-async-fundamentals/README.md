# Day 8 — Async Fundamentals

## Why this matters
Most of what a backend does is *wait* — waiting for a database query, waiting
for another API to respond, waiting for a file to read. `async`/`await` lets
your program start several of those waits at the same time instead of doing
them one after another, without needing multiple threads or processes. This
is not optional knowledge for FastAPI — Week 3 uses `async def` on nearly
every endpoint.

## Where you'll actually use this
- **FastAPI endpoints (Week 3 onward)**: `async def` routes, `await`ing
  database calls and outbound HTTP requests, are the default way modern
  Python web backends are written.
- **httpx.AsyncClient (Day 14)**: calling an external API from inside your
  own API — if you don't understand `await` today, that day will feel like
  memorizing incantations instead of understanding what's happening.
- **Any I/O-bound workload**: scraping multiple URLs, calling multiple
  microservices, reading multiple files — anywhere you're waiting on
  something external, concurrency (not necessarily more CPU) is the win.

## Concepts & syntax

### `async def` and `await`
```python
import asyncio

async def fetch_data(name, delay):
    await asyncio.sleep(delay)   # simulates waiting on I/O
    return f"{name} done"
```
`async def` marks a function as a **coroutine function** — calling it doesn't
run the body immediately, it returns a coroutine object (similar to how
calling a generator function doesn't run it either). `await` is how you
actually run a coroutine and get its result, but `await` can only be used
*inside another `async def` function*.
Docs: https://docs.python.org/3/library/asyncio-task.html

### Running a coroutine from regular (sync) code
```python
asyncio.run(fetch_data("x", 1))
```
`asyncio.run(...)` is the entry point — it creates an event loop, runs your
top-level coroutine to completion, and cleans up. You call this once, from
regular code, to "start" the async world. You'll see this exact pattern in
every test in this folder.
Docs: https://docs.python.org/3/library/asyncio-runner.html#asyncio.run

### Sequential awaits (no speedup)
```python
async def fetch_sequentially(tasks):
    results = []
    for name, delay in tasks:
        result = await fetch_data(name, delay)   # waits for EACH one fully
        results.append(result)
    return results
```
Each `await` blocks until that specific call finishes before moving to the
next line. Three 1-second calls awaited like this take ~3 seconds total —
exactly like normal synchronous code. Async by itself doesn't make anything
faster; you have to explicitly ask for concurrency.

### `asyncio.gather` (actual concurrency)
```python
async def fetch_concurrently(tasks):
    return await asyncio.gather(*(fetch_data(name, delay) for name, delay in tasks))
```
`gather` starts all the given coroutines running *at the same time* and waits
for all of them to finish, returning their results in the same order you
passed them in (not the order they finished in). Three 1-second calls run
concurrently take ~1 second total, not 3.
Docs: https://docs.python.org/3/library/asyncio-task.html#asyncio.gather

## The task
Open `starter.py`. Implement:
1. `fetch_data(name, delay)` — `await asyncio.sleep(delay)`, then return
   `f"{name} done"`.
2. `fetch_sequentially(tasks)` — `tasks` is a list of `(name, delay)` tuples.
   Await each one *one at a time*, return results in order.
3. `fetch_concurrently(tasks)` — same input, but run all of them at once
   with `asyncio.gather`, returning results in the same order as the input.

## Run it
```bash
cd day08-async-fundamentals
pytest -v
```
One test explicitly checks that `fetch_concurrently` is meaningfully faster
than `fetch_sequentially` on the same input — that's the whole point made
concrete, not just an assertion on returned values.

## Common pitfalls
- Calling an `async def` function *without* `await` (e.g. `fetch_data("x", 1)`
  by itself) doesn't run it — it just creates a coroutine object and does
  nothing with it. Python will actually warn you about this
  ("coroutine was never awaited") if it happens.
- `await` only works inside another `async def`. You can't `await` something
  directly in a normal synchronous function — that's exactly why
  `asyncio.run(...)` exists, as the bridge from sync to async.
- `asyncio.gather(*coroutines)` needs the star (`*`) to unpack a list of
  coroutines into separate arguments — `asyncio.gather(coroutines)` (a single
  list argument) is a common typo that behaves very differently.

## Stretch goal (optional)
Add a fourth function, `fetch_with_timeout(name, delay, timeout)`, using
`asyncio.wait_for(fetch_data(name, delay), timeout=timeout)` — if `delay`
exceeds `timeout`, it should raise `asyncio.TimeoutError` instead of hanging.
This is the exact mechanism you'll use in Day 14 to stop a slow external API
call from blocking your endpoint forever.

## Further reading
- asyncio's own high-level "coroutines and tasks" guide (the best single
  starting point): https://docs.python.org/3/library/asyncio-task.html
- Real Python's async intro (longer, more examples):
  https://realpython.com/async-io-python/
