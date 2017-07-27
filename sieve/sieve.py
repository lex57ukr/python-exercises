import itertools


def sieve(limit):
    primes = itertools.takewhile(
        lambda n: n <= limit,
        prime_numbers()
    )

    return list(primes)


def prime_numbers():
    def sieve_multiples_of(iterator, prime):
        def acc(count, number):
            if count == 1:
                return (prime, False)
            else:
                return (count - 1, number)

        return accumulate_with_return(iterator, acc, prime * (prime - 1))

    def search_for_primes(remaining_numbers):
        prime = find(remaining_numbers, lambda n: n != False)
        return (
            sieve_multiples_of(remaining_numbers, prime),
            prime
        )

    numbers_from_two = itertools.count(2)
    return unfold_with_return(numbers_from_two, search_for_primes)


def find(iterator, predicate):
    while True:
        try:
            value = next(iterator)
        except StopIteration:
            return None
        else:
            if predicate(value):
                return value


def accumulate_with_return(iterator, function, init):
    state = init
    for item in iterator:
        state, result = function(state, item)
        yield result


def unfold_with_return(seed, function):
    state = seed
    while True:
        state, result = function(state)
        yield result
