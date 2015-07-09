import atbash_encoding

def encode(clear):
    return clear.encode('atbash')

decode = encode  # This cipher is symmetrical

