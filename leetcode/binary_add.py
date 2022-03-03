def add_binary(a,b):
    al=-len(a)
    bl=-len(b)
    carry=0
    res=""
    i=-1

    while i>=al or i>=bl:
        if i>=al:
            a_bit=int(a[i])
        else:
            a_bit=0
        
        if i>=bl:
            b_bit=int(b[i])
        else:
            b_bit=0

        add=a_bit+b_bit+carry
        res=str(add%2)+res
        carry=add//2

        i=i-1

    if carry==1:
        return "1"+res
    else:
        return res


print(add_binary("11","1"))
    