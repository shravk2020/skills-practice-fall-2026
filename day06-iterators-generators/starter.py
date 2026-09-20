def read_large_numbers(n):
    """Return the first n square numbers: 1, 4, 9, 16, ...

    TODO: convert this into a generator function. Change `return` into a
    loop that `yield`s one square at a time, instead of building a list.
    """
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result


def first_n_over_threshold(numbers, threshold, n):
    """numbers is any iterable (possibly infinite). Return a list of the
    first n values from numbers that are greater than threshold.

    TODO: rewrite using a generator expression + itertools.islice, so this
    never asks `numbers` for more values than it actually needs.
    """
    result = []
    for x in numbers:
        if x > threshold:
            result.append(x)
        if len(result) == n:
            break
    return result


def group_consecutive_duplicates(items):
    """items is a list like [1, 1, 2, 2, 2, 3, 1, 1].
    Return a list of (value, count) tuples for consecutive runs:
    [(1, 2), (2, 3), (3, 1), (1, 2)]

    TODO: rewrite using itertools.groupby.
    """
    result = []
    if not items:
        return result
    current = items[0]
    count = 1
    for item in items[1:]:
        if item == current:
            count += 1
        else:
            result.append((current, count))
            current = item
            count = 1
    result.append((current, count))
    return result
