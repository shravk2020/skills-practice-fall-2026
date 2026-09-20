def get_even_squares(nums):
    return [n * n for n in nums if n % 2 == 0]


def build_name_lookup(people):
    return {id_: name for id_, name in people}


def pair_with_index(items):
    return [f"{i}: {item}" for i, item in enumerate(items)]
