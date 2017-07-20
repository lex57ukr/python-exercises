from re import sub


def decode(text):
    def _explode(match):
        rept = match.group(1)
        char = match.group(2)

        if not rept:
            return char
        else:
            return char * int(rept)

    return sub(r'(\d*)(.)', _explode, text)


def encode(text):
    def _implode(match):
        rept = len(match.group(0))
        char = match.group(1)

        if rept == 1:
            return char
        else:
            return str(rept) + char

    return sub(r'([A-Za-z\s])\1*', _implode, text)
