def is_increasing(ns):
    if len(ns)<2:
        return True
    for i in range(1, len(ns)):
        if ns[i]<ns[i-1]:
            return False
    return True