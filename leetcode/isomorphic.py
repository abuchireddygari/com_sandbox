def is_isomorphic(s,t):
    if len(s)!=len(t):
        return False
    ds={}
    dt={}
    
    for i in range(len(s)):
        ds[s[i]]=ds.get(s[i],0)+1
        dt[t[i]]=dt.get(t[i],0)+1
    print(ds)
    print(dt)
    
    return sorted(ds.values())==sorted(dt.values())

print(is_isomorphic("bbbaaaba","aaabbbba"))