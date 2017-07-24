def slices(series, size):
    if not 1 <= size <= len(series):
        raise ValueError('Invalid size %r for %r' % (size, series))

    numbers = [int(n) for n in series]
    return [numbers[i: i+size] for i in range(len(numbers) - size + 1)]
