from textwrap import wrap


def proteins(strand):
    valid_codons = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP',
    }

    codons = wrap(strand, 3)
    result = []

    if not strand.startswith('UAA') and not strand.startswith('UAG') and not strand.startswith('UGA'):
        for codon in codons:
            if codon in valid_codons.keys() and valid_codons[codon] != 'STOP' and valid_codons[codon] not in result:
                result.append(valid_codons[codon])
            else:
                break

    return result
