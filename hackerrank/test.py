alphabets="abcdefghijklmnopqrstuvwxyz"
cnt=1
weight={}
for alphabet in alphabets:
    weight[alphabet]=cnt
    cnt=cnt+1

print(weight)

s="abbccccdddd"

pl=None
wsum=0
wdict={}
for l in s:
    if l==pl:
        wsum=wsum+weight[l]
        wdict[wsum]=1
    else:
        wsum=weight[l]
        wdict[wsum]=1
        pl=l
print(wdict)
