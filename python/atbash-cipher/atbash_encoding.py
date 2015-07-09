""" This module registers the atbash encoding when imported. """

from codecs import register, CodecInfo
from string import ascii_lowercase, maketrans, translate

_trans = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def _atbash(input, _=None):
    return translate(input.lower(), _trans), len(input)

def _search(name):
    if name == 'atbash':
        return CodecInfo(_atbash, _atbash)
    return None

register(_search)
