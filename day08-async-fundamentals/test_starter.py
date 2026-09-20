import asyncio
import time
from starter import fetch_data, fetch_sequentially, fetch_concurrently

TASKS = [("a", 0.1), ("b", 0.1), ("c", 0.1)]


def test_fetch_data_returns_expected_string():
    result = asyncio.run(fetch_data("x", 0.01))
    assert result == "x done"


def test_fetch_sequentially_returns_all_results_in_order():
    results = asyncio.run(fetch_sequentially(TASKS))
    assert results == ["a done", "b done", "c done"]


def test_fetch_concurrently_returns_all_results_in_order():
    results = asyncio.run(fetch_concurrently(TASKS))
    assert results == ["a done", "b done", "c done"]


def test_concurrently_is_faster_than_sequentially():
    start = time.perf_counter()
    asyncio.run(fetch_sequentially(TASKS))
    sequential_time = time.perf_counter() - start

    start = time.perf_counter()
    asyncio.run(fetch_concurrently(TASKS))
    concurrent_time = time.perf_counter() - start

    # 3 tasks x 0.1s: sequential should take ~0.3s, concurrent ~0.1s.
    # Generous margin to avoid flakiness on a slow machine.
    assert concurrent_time < sequential_time * 0.6
