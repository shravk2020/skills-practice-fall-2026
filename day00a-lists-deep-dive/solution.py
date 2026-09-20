def add_if_missing(items, value):
    if value not in items:
        items.append(value)
    return items


def combine(a, b):
    return a + b


def take_last(items, n):
    if n == 0:
        return []
    return items[-n:]


def every_other_reversed(items):
    return items[::-2]


def remove_and_return_middle(items):
    middle_index = len(items) // 2
    return items.pop(middle_index)


def safe_index(items, value):
    try:
        return items.index(value)
    except ValueError:
        return -1


def sort_by_length_desc(words):
    return sorted(words, key=len, reverse=True)


def independent_copy(items):
    return items.copy()
