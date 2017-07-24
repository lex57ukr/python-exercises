def slices(series, size):
    if not 1 <= size <= len(series):
        raise ValueError('Invalid size %r for %r' % (size, series))

    def _cast_slice_at(i):
        return [int(n) for n in series[i: i+size]]

    return [_cast_slice_at(i) for i in range(len(series) - size + 1)]
