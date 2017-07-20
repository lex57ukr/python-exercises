ALPHABET_LENGTH = 26


def is_pangram(sentence):
    alpha = set(as_lowercase_letters_only(sentence))
    return len(alpha) == ALPHABET_LENGTH


def as_lowercase_letters_only(text):
    return filter(str.isalpha, str.lower(text))
