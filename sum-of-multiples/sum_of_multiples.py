def sum_of_multiples(number, factors):
    def _is_mul(n):
        return any((n for f in factors if n % f == 0))

    return sum([n for n in range(1, number) if _is_mul(n)])
