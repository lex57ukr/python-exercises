def distance(dna_x, dna_y):
    if len(dna_x) != len(dna_y):
        raise ValueError

    return len([1 for x, y in zip(dna_x, dna_y) if x != y])
