def detect_anagrams(word, candidates):
    accept = anagram_detector_for(word)
    return [w for w in candidates if accept(w)]

def anagram_detector_for(word):
    def _alpa(word):
        return sorted(word.lower())

    lower = word.lower()
    alpha = _alpa(word)

    def _is_my_anagram(other):
        return other.lower() != lower and _alpa(other) == alpha

    return _is_my_anagram
