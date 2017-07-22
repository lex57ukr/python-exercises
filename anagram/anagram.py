def detect_anagrams(base, candidates):
    def _alpa(word):
        a = list(word)
        a.sort()
        return a

    lower_base = base.lower()
    alpha_base = _alpa(lower_base)

    def _is_anagram(word):
        lower = word.lower()
        return lower != lower_base and _alpa(lower) == alpha_base

    return [word for word in candidates if _is_anagram(word)]
