from functools import partial
from itertools import zip_longest


def encode(text):
    @group_output_text(group_size=5)
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

def group_output_text(function=None, group_size=5, fill_value=''):
    """Group output text by specified group size"""
    if function is None:
        return partial(
            group_output_text,
            group_size=group_size,
            fill_value=fill_value
        )

    def _wrapped(*args, **kwargs):
        iterator = function(*args, **kwargs)

        sequence = [iter(iterator)] * group_size
        groups = zip_longest(*sequence, fillvalue=fill_value)

        return [''.join(list(g)) for g in groups]

    return _wrapped
