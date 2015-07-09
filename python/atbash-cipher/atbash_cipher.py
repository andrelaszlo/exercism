from codecs import register, CodecInfo
from string import ascii_lowercase, maketrans, translate
import re

# Register an atbash encoding
# Would be in a separate module, but exercism doesn't support submitting
# multiple files (yet!)

_pattern = re.compile(r'[^a-z1-9]')

_trans = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def _atbash(input, group=False):
    raw = translate(_pattern.sub('', input.lower()), _trans)
    if not group:
        return raw, len(raw)
    grouped = [raw[i:i+5] for i in range(0, len(raw), 5)]
    return ' '.join(grouped), len(input)

def _search(name):
    if name == 'atbash':
        return CodecInfo(lambda s, _=None: _atbash(s, True),
                         lambda s, _=None: _atbash(s, False))
    return None

register(_search)

# Module interface

def encode(clear):
    return clear.encode('atbash')

def decode(cypher):
    return cypher.decode('atbash')

