def unique_words(text):
    return set(text.lower().split())


def shared_tags(tags1, tags2):
    return set(tags1) & set(tags2)


def only_in_first(a, b):
    return set(a) - set(b)


def clean_sentence(s):
    return s.strip().lower()


def split_first_rest(items):
    first, *rest = items
    return (first, rest)


def title_case_sentence(s):
    return " ".join(word.title() for word in s.split())
