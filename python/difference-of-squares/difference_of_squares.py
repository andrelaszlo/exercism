from future_builtins import map

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)

def sum_of_squares(n):
    return sum(map(lambda x: x**2, xrange(n+1)))

def square_of_sum(n):
    return sum(xrange(n+1))**2
