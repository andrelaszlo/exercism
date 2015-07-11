import operator

def slices(digits, length):
    """ Generator version of the slices function from the series exercise. """
    if len(digits) < length or length < 1:
        raise ValueError("Slice length %d is too long" % length)

    digit_array = [int(c) for c in digits]
    for i in range(len(digits) - length + 1):
        yield digit_array[i:i+length]

def largest_product(digits, length):
    _slices = slices(digits, length)
    return max([reduce(operator.mul, _slice) for _slice in _slices])
