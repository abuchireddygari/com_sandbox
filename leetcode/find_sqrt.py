def get_sqrt(x):

    low=0
    high=x

    while low<=high:
        mid=(low+high)//2

        if mid*mid>x:
            high=mid-1
        elif mid*mid<x:
            low=mid+1
        else:
            return mid
    return high

print(get_sqrt(25))
print(get_sqrt(8))
