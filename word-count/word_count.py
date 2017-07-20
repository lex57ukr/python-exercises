from re import split
from collections import Counter


def word_count(sentence):
    words = as_lowercase_words(sentence)
    return dict(Counter(words))


def as_lowercase_words(sentence):
    words = split(r'[_\s\W]', sentence)
    return [str.lower(word) for word in words if word != '']
