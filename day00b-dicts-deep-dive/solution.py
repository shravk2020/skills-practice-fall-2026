def get_or_default(d, key, default):
    return d.get(key, default)


def increment_count(counts, key):
    counts[key] = counts.get(key, 0) + 1
    return counts


def merge_configs(base, override):
    return base | override


def pop_or_default(d, key, default):
    return d.pop(key, default)


def invert(d):
    return {value: key for key, value in d.items()}


def common_keys(d1, d2):
    return d1.keys() & d2.keys()
