def mode(ns):
    count = {}
    for n in ns:
        if n not in count:
            count[n]=0
        count[n]+=1
    return max(count.items(), key=lambda pair: pair[1])[0]
