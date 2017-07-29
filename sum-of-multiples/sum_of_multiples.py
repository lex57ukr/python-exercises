def sum_of_multiples(number, factors):
    multiples = set().union(*(
        set(range(f, number, f)) for f in factors
    ))

    return sum(multiples)
