from codecs import register, CodecInfo
from string import ascii_lowercase, maketrans, translate
import re

# Register an atbash encoding
# Would be in a separate module, but exercism doesn't support submitting
# multiple files (yet!)

_BLOCK_SIZE = 5
_PATTERN = re.compile(r'[^a-z1-9]')
_TRANS = maketrans(ascii_lowercase, ascii_lowercase[::-1])

def _atbash(txt, group=False):
    raw = translate(_PATTERN.sub('', txt.lower()), _TRANS)
    if not group:
        return raw, len(txt)
    grouped = [raw[i:i + _BLOCK_SIZE]
               for i in range(0, len(raw), _BLOCK_SIZE)]
    return ' '.join(grouped), len(txt)

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

