def natural(func):
    """Call a func on a range of natural numbers"""
    return lambda num: func(range(1, num + 1))


@natural
def square_of_sum(numbers):
    """Compute a square of a sum of natural numbers"""
    return sum(numbers)**2


@natural
def sum_of_squares(numbers):
    """Compute a sum of squares of natural numbers"""
    return sum(n**2 for n in numbers)


def difference(n):
    """Compute a diff between square_of_sum and sum_of_squares"""
    return square_of_sum(n) - sum_of_squares(n)
