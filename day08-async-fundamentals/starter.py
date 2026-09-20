import asyncio


async def fetch_data(name, delay):
    """Simulates an I/O call that takes `delay` seconds.

    TODO: await asyncio.sleep(delay), then return f"{name} done".
    """
    pass


async def fetch_sequentially(tasks):
    """tasks is a list of (name, delay) tuples. Await fetch_data(name, delay)
    for each tuple ONE AT A TIME (not concurrently). Return a list of
    results in the same order as the input.

    TODO: implement.
    """
    pass


async def fetch_concurrently(tasks):
    """Same input as fetch_sequentially, but run all of them AT THE SAME
    TIME using asyncio.gather. Return a list of results in the same order
    as the input tasks.

    TODO: implement using asyncio.gather.
    """
    pass
