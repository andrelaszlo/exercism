_dna_to_rna_map = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(strand):
    """ Given a DNA strand, returns its RNA complement (per RNA transcription).
    """
    return ''.join(_dna_to_rna_map[nucleotide]
                   for nucleotide in strand)
