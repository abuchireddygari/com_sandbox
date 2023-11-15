def anagram(s,t):
    
    if len(s)!=len(t):
        return False

    ds={}
    dt={}

    for i in range(len(s)):
        ds[s[i]]=ds.get(s[i],0)+1
        dt[t[i]]=dt.get(t[i],0)+1
    
    return ds==dt

print(anagram("anagram","nagaram"))
print(anagram("cat","rat"))