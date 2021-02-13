def frequencies(xs):
    res = {}
    for x in xs:
        if x in res:
            res[x]+=1
        else:
            res[x]=1
    return res