def get_even_squares(nums):
    """Return the square of every even number in nums, in order.

    TODO: rewrite the body using a list comprehension.
    """
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n * n)
    return result


def build_name_lookup(people):
    """people is a list of (id, name) tuples.
    Return a dict mapping id -> name.

    TODO: rewrite the body using a dict comprehension (and tuple unpacking
    in the loop variable, e.g. `for id_, name in people`).
    """
    result = {}
    for pair in people:
        id_ = pair[0]
        name = pair[1]
        result[id_] = name
    return result


def pair_with_index(items):
    """Return a list of "index: item" strings for each item in items.

    TODO: rewrite the body using enumerate() instead of a manual counter.
    """
    result = []
    i = 0
    for item in items:
        result.append(f"{i}: {item}")
        i += 1
    return result
