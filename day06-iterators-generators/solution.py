import itertools


def read_large_numbers(n):
    for i in range(1, n + 1):
        yield i * i


def first_n_over_threshold(numbers, threshold, n):
    matches = (x for x in numbers if x > threshold)
    return list(itertools.islice(matches, n))


def group_consecutive_duplicates(items):
    return [(value, len(list(group))) for value, group in itertools.groupby(items)]
