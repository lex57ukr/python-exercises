def abbreviate(text):
    def _first_title_letters():
        return [c for c in text.title() if c.isupper()]
    return ''.join(_first_title_letters())
