from string import ascii_lowercase, maketrans, translate

table = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(clear):
    return translate(clear.lower(), table)

decode = encode  # This cipher is symmetrical
