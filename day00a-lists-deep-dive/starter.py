def add_if_missing(items, value):
    """Append value to items only if it's not already present.
    Mutates items in place. Return items.

    TODO: use the `in` operator + .append().
    """
    pass


def combine(a, b):
    """Return a NEW list containing all of a's items followed by all of b's
    items. Must NOT modify a or b.

    TODO: use + (not .extend(), which would mutate a).
    """
    pass


def take_last(items, n):
    """Return the last n items as a new list, using slicing.
    If n is 0, return an empty list.

    TODO: use slicing.
    """
    pass


def every_other_reversed(items):
    """Return every other item, starting from the last one, going backwards.
    e.g. [1, 2, 3, 4, 5, 6] -> [6, 4, 2]

    TODO: one slice expression with a negative step.
    """
    pass


def remove_and_return_middle(items):
    """items has an odd length. Remove AND return the middle element.
    Mutates items in place.

    TODO: use .pop(index).
    """
    pass


def safe_index(items, value):
    """Return the index of value in items, or -1 if it's not present.

    TODO: use .index() inside a try/except ValueError.
    """
    pass


def sort_by_length_desc(words):
    """Return a NEW list of words sorted by length, longest first.
    Must NOT modify the original list.

    TODO: use sorted() (not .sort()) with key= and reverse=.
    """
    pass


def independent_copy(items):
    """Return a copy of items such that modifying the copy does NOT affect
    the original.

    TODO: use .copy() (or items[:]) -- not plain assignment.
    """
    pass
