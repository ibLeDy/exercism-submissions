def distance(strand_a, strand_b):

    if len(strand_a) == len(strand_b):
        return sum(1 for i in range(len(strand_a)) if strand_a[i] != strand_b[i])

    else:
        raise ValueError("Strands provided are not the same length")
