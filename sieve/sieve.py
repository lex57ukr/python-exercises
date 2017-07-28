def sieve(limit):
    def _prime_numbers():
        candidates = [True] * (limit + 1)

        def _mark_multiples_of(prime):
            for i in range(prime * 2, limit + 1, prime):
                candidates[i] = False

        for i in range(2, limit + 1):
            if not candidates[i]:
                continue

            _mark_multiples_of(i)
            yield i

    return list(_prime_numbers())
