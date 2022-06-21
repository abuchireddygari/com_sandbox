def first_uniq_chr(s):
    cmap={}
    for c in s:
        cmap[c]=cmap.get(c,0)+1
    print(cmap)
    for i,v in enumerate(s):
        if cmap[v]<2:
            return i
    return -1
print(first_uniq_chr("leetcode"))
print(first_uniq_chr("loveleetcode"))
print(first_uniq_chr("aabb"))