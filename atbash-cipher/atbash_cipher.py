from functools import partial
from textwrap import wrap


def encode(text):
    @cipher_formatter
    def _encoded_text():
        tmap = {c: e for c, e in _transcoded_mappings()}
        return (tmap.setdefault(c.lower(), c) for c in text if c.isalnum())

    return ' '.join(_encoded_text())


def decode(text):
    def _decoded_text():
        tmap = {e: c for c, e in _transcoded_mappings()}
        return (tmap.setdefault(c, c) for c in text if c.isalnum())

    return ''.join(_decoded_text())


def _transcoded_mappings():
    start = ord('a')
    end = ord('z')
    for c in range(start, end + 1):
        yield (chr(c), chr(end + start - c))


def cipher_formatter(function=None, group_size=5):
    if function is None:
        return partial(cipher_formatter, group_size=group_size)

    def _wrapped(*args, **kwargs):
        text = ''.join(function(*args, **kwargs))
        return wrap(text, width=group_size)

    return _wrapped
