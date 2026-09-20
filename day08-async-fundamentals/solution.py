import asyncio


async def fetch_data(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"


async def fetch_sequentially(tasks):
    results = []
    for name, delay in tasks:
        result = await fetch_data(name, delay)
        results.append(result)
    return results


async def fetch_concurrently(tasks):
    return list(await asyncio.gather(*(fetch_data(name, delay) for name, delay in tasks)))
