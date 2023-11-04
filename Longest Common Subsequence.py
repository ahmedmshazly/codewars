def lcs(x, y):
    r=''
    l = list(x)
    idx=0
    if len(y)==0:
        return ""
    for c in y:
        if c in l :
            idx = l.index(c)
            r+=c    
            l = l[idx+1:]
        else:
            pass
        
    return "" if (len(r)==0) else r

print(lcs("a", "a"))