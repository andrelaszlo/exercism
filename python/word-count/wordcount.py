from collections import defaultdict

def word_count(sentence):
    count = defaultdict(lambda: 0)
    for word in sentence.split():
        count[word] += 1
    return count
