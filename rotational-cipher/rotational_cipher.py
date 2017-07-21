def rotate(text, shift):
    def _rot(c):
        def _from(base):
            b = ord(base)
            return chr(b + (ord(c) - b + shift) % 26)

        if 'A' <= c <= 'Z':
            return _from('A')

        if 'a' <= c <= 'z':
            return _from('a')

        return c

    return ''.join(_rot(c) for c in text)
