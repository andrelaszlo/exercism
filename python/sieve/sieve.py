def sieve(n):
    """List all the primes between 2 and n (inclusively)."""
    p = list(range(2, n+1))
    for i in range(2, n+1):
        p = [x for x in p if x == i or x % i != 0]
    return p
