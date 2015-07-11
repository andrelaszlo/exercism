def _multiples(n, m):
    if m == 0: return set()
    return set(i*m for i in range(1, int(n/m)+1) if i*m < n)

def sum_of_multiples(n, factors=[3, 5]):
    return sum(reduce(set.union, [_multiples(n, m) for m in factors]))
