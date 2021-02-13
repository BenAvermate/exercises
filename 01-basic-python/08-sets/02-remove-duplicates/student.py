def remove_duplicates(xs):
    found=set()
    res=[]
    for x in xs:
        if x not in found:
            res.append(x)
            found.add(x)
    return res