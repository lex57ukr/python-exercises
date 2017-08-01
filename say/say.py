import math
import itertools


_MAX_POWER = 12
MAX_NUMBER = 10 ** _MAX_POWER - 1


def say(number):
    if not 0 <= number <= MAX_NUMBER:
        raise AttributeError(
            'Natural numbers thru %r only' % (MAX_NUMBER)
        )

    if number == 0:
        return _digit(0)

    return ' '.join([
        _say_thousands(group, power)
        for power, group in group_thousands(number)
        if sum(group) != 0
    ])

def _digit(n):
    return [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ][n]


def _ten(n):
    return [
        'ten',
        'elleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'ninteen'
    ][n]


def _tens(n):
    return {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninty'
    }[n]


def _hundreds(n):
    return '%s hundred' % (_digit(n))


def _thru99(tens, n):
    if tens == 0:
        return _digit(n)
    elif tens == 1:
        return _ten(n)
    elif n == 0:
        return _tens(tens)
    else:
        return '%s-%s' % (_tens(tens), _digit(n))


def _say_hundreds(group):
    hundreds, tens, n = group
    if hundreds == 0:
        return _thru99(tens, n)
    elif tens == 0 and n == 0:
        return _hundreds(hundreds)
    else:
        return '%s and %s' % (_hundreds(hundreds), _thru99(tens, n))


def _say_thousands(group, power=0):
    if power == 0:
        return _say_hundreds(group)

    scale = {
        1: 'thousand',
        2: 'million',
        3: 'billion',
        4: 'trillion'
    }[power]
    return '%s %s' % (_say_hundreds(group), scale)


def group_thousands(number):
    """ Group a number by thousands

        Returns an iterable of tuples (power, tri) ordered
        naturally, where:
            power of 1,000 to designate the scale of the group
            tri is a tuple of (h,t,d)

        For example, [(1,(0,1,0)), (0,(1,2,3))] for 10123
    """
    def _weigh(mod):
        return int(10 * (number % mod) / mod)

    def _in_base10():
        digits = math.floor(math.log10(number)) + 1
        return [_weigh(10 ** p) for p in range(1, digits + 1)]

    groups = [
        tuple(reversed(group)) for group in
        itertools.zip_longest(*[iter(_in_base10())]*3, fillvalue=0)
    ]

    # scaled groups of thousands must be put in their natural order
    scaled_groups = enumerate(groups)
    return reversed(list(scaled_groups))
