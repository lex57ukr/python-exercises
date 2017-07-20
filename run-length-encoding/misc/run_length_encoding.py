"""Iteration 2: use itertools"""
from itertools import groupby


def decode(text):
    def _groups():
        repeat_buff = ''
        for char in text:
            if char.isdigit():
                repeat_buff += char
            elif not repeat_buff:
                yield (1, char)
            else:
                repeat = int(repeat_buff)
                repeat_buff = ''
                yield (repeat, char)

    def _decode(repeat, char):
        return char * repeat

    return compose(_groups(), _decode)


def encode(text):
    def _groups():
        for char, group in groupby(text):
            repeat = len(list(group))
            yield (repeat, char)

    def _encode(repeat, char):
        if repeat == 1:
            return char
        else:
            return str(repeat) + char

    return compose(_groups(), _encode)


def compose(groups, formatter):
    return ''.join(formatter(r, c) for r, c in groups)
