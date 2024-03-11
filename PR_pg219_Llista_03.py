def norep(v):
    u = []
    for e in v:
        if e not in u:
            u.append(e)
    return u 


print(max([1,2,3,4,3,2,5,3]))