def slices(digits, length):
    if length > len(digits) or length < 1:
        raise ValueError("Slice length %d is too long" % length)

    digit_array = [int(c) for c in digits]
    slices = []

    for i in range(len(digits) - length + 1):
        slices.append(digit_array[i:i+length])

    return slices
