def sum_of_multiples(n, factors=[3, 5]):
    return sum(reduce(set.union,
                      [set(range(m, n, m)) if m != 0 else set()
                       for m in factors]))
