def to_rna(dna_strand):
    nucleotides = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    rna_strand = ''
    for nucleotide in dna_strand:
        rna_strand += nucleotides.get(nucleotide, nucleotide)
    return rna_strand
