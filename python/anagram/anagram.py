from collections import Counter
from functools import partial

def is_anagram(word, candidate):
    word = word.lower()
    candidate = candidate.lower()
    if word == candidate:
        return False
    return Counter(word) == Counter(candidate)

def detect_anagrams(word, candidates):
    return filter(partial(is_anagram, word), candidates)
