def dup(arry):
    l = []
    r=[]
    s=''
    for i in arry:
        for idx, c in enumerate(i):
            if idx == 0:
                l.append(c)
                continue
            else:
                l.append(c) if i[idx-1] != c else ""
        s+="".join(l)
        l=[]
        r.append(s)
        s=''
    return r


print(dup(["abracadabra","allottee","assessee"]))