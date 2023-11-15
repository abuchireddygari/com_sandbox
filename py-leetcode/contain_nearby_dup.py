def containsNearbyDuplicate(nums, k):
    d={}
    for i,v in enumerate(nums):
        if v in d and i-d[v]<=k:
            return True
        d[v]=i
    
    return False


print(containsNearbyDuplicate([1,2,3,1],3))

print(containsNearbyDuplicate([1,0,1,1],1))

print(containsNearbyDuplicate([1,2,3,1,2,3],2))
