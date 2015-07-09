import functools
from string import ascii_lowercase

table = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))

def char_trans(c):
    if c.lower() in table:
        return table[c.lower()]
    return c

def encode(clear):
    return ''.join(char_trans(c) for c in clear)

decode = encode
