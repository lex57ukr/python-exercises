def square_of_sum(n):
    """Compute a square of a sum of the first n-natural numbers"""
    return (n * (n + 1) / 2) ** 2


def sum_of_squares(n):
    """Compute a sum of squares of the first n-natural numbers"""
    return (n * (n + 1) * (2 * n + 1)) / 6


def difference(n):
    """Compute a diff between square_of_sum and sum_of_squares"""
    return square_of_sum(n) - sum_of_squares(n)
