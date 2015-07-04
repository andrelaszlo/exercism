from operator import ne

def distance(a, b):
    return len(filter(lambda x: ne(*x), zip(a, b)))
