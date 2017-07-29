def sum_of_multiples(number, factors):
    def _multiples():
        def _is_mul(n):
            return any((n % f == 0 for f in factors))
        return [n for n in range(1, number) if _is_mul(n)]
    return sum(_multiples())
