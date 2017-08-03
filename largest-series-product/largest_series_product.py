from operator import mul
from functools import reduce


def largest_product(sequence, series_length):
    if not 0 <= series_length <= len(sequence):
        raise ValueError

    def _groups():
        for i in range(len(sequence) + 1 - series_length):
            yield tuple(int(x) for x in sequence[i: i+series_length])

    return max(reduce(mul, g, 1) for g in _groups())
