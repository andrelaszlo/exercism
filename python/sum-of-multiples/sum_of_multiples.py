def sum_of_multiples(n, fs=[3, 5]):
    return sum(i for i in range(n) if any(i % f == 0 for f in fs if fs))
