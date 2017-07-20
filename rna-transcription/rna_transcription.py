def to_rna(dna):
    nucleotides = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    try:
        rna = [nucleotides[c] for c in dna]
    except KeyError:
        return ''
    else:
        return ''.join(rna)
