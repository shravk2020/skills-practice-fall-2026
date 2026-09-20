def get_or_default(d, key, default):
    """Return d[key] if present, otherwise return default. Must NOT modify d.

    TODO: use .get().
    """
    pass


def increment_count(counts, key):
    """counts is a dict mapping some key -> int count. Increment counts[key]
    by 1, adding it with a starting value of 0 first if it's not present yet.
    Mutates counts in place. Return counts.

    TODO: use .get() (or .setdefault()) -- not `if key in counts: ... else: ...`.
    """
    pass


def merge_configs(base, override):
    """Return a NEW dict: base's keys/values, with override's keys/values
    layered on top (override wins on conflicts). Must NOT modify base or
    override.

    TODO: use the | operator.
    """
    pass


def pop_or_default(d, key, default):
    """Remove key from d and return its value, if present. If key is not
    present, return default WITHOUT raising an error, and don't add
    anything to d.

    TODO: use .pop() with a default argument.
    """
    pass


def invert(d):
    """Return a NEW dict with d's keys and values swapped, e.g.
    {"a": 1, "b": 2} -> {1: "a", 2: "b"}. Assume all of d's values are
    unique (safe to use as keys).

    TODO: use a dict comprehension over d.items().
    """
    pass


def common_keys(d1, d2):
    """Return a set of keys that appear in BOTH d1 and d2.

    TODO: use .keys() with the & (intersection) operator.
    """
    pass
