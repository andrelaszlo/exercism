def sum_of_multiples(n, f=[3, 5]):
    return sum(set(reduce(lambda a,m: a+m, (range(m,n,m) for m in f if m), [])))
