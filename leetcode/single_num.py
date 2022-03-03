def single_number(nums):
    i=0
    l=len(nums)-1
    while i<=l:
        j=0
        stop_looping=False
        while j<=l and not stop_looping:
            if nums[i]==nums[j] and i!=j:
                stop_looping=True
            else:
                j=j+1

        if not stop_looping:
            return nums[i]
        i=i+1

def single_number2(nums):
    res=0
    for num in nums:
        res=res^num
        



print(single_number([4,1,2,1,2]))
