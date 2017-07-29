import textwrap
import functools


def encode(text):
    @wrap_output(width=5)
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


def wrap_output(function=None, width=70):
    """Decorate a function to wrap its output by width-sized groups"""
    if function is None:
        return functools.partial(wrap_output, width=width)

    def _wrapped(*args, **kwargs):
        text = ''.join(function(*args, **kwargs))
        return textwrap.wrap(text, width=width)

    return _wrapped
