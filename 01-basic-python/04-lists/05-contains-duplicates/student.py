def contains_duplicates(xs):
    if len(xs)<2:
        return False
    xs = sorted(xs)
    for i in range(len(xs)-1):
        if xs[i]==xs[i+1]: return True
    return False