def distance(strand_a, strand_b):
    if strand_b==strand_a:
        return 0
    elif len(strand_b)!=len(strand_a):
        raise ValueError("Both values should be of equal length")
    else:
        total=0
        for i, k in enumerate(strand_a):
            if k != strand_b[i]:
                total+=1
        return (total)