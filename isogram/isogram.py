from collections import Counter


def is_isogram(word):
    cnt = Counter(as_lowercase_letters_only(word))
    return not cnt or cnt.most_common(1)[0][1] == 1


def as_lowercase_letters_only(word):
    return filter(str.isalpha, str.lower(word))
