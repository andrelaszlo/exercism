from codecs import register, CodecInfo
from string import ascii_lowercase, maketrans, translate

# Register an atbash encoding
# Would be in a separate module, but exercism doesn't support submitting
# multiple files (yet!)

_trans = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def _atbash(input, _=None):
    return translate(input.lower(), _trans), len(input)

def _search(name):
    if name == 'atbash':
        return CodecInfo(_atbash, _atbash)
    return None

register(_search)

# Module interface

def encode(clear):
    return clear.encode('atbash')

decode = encode  # This cipher is symmetrical

